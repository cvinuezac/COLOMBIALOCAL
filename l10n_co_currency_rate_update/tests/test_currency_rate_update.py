# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from datetime import date
from dateutil.relativedelta import relativedelta
from unittest import mock

from odoo import fields
from odoo.tests.common import TransactionCase

_module_ns = "odoo.addons.l10n_co_currency_rate_update"
_file_ns = _module_ns + ".models.res_currency_rate_provider_FSC"
_FSC_provider_class = _file_ns + ".ResCurrencyRateProviderFSC"


class TestCurrencyRateUpdate(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Company = cls.env["res.company"]
        cls.CurrencyRate = cls.env["res.currency.rate"]
        cls.CurrencyRateProvider = cls.env["res.currency.rate.provider"]

        cls.today = fields.Date.today()
        cls.usd_currency = cls.env.ref("base.USD")
        cls.usd_currency.write({"active": True})
        cls.cop_currency = cls.env.ref("base.COP")
        cls.cop_currency.write({"active": True})
        cls.company = cls.Company.create(
            {
                "name": "Test company COP",
                "currency_id": cls.cop_currency.id,
            }
        )
        cls.env.user.company_ids += cls.company
        cls.env.user.company_id = cls.company
        cls.fsc_provider = cls.CurrencyRateProvider.create(
            {
                "service": "FSC",
                "currency_ids": [
                    (4, cls.usd_currency.id),
                    (4, cls.cop_currency.id),
                ],
            }
        )
        cls.CurrencyRate.search([]).unlink()

    def test_supported_currencies_FSC(self):
        self.fsc_provider._get_supported_currencies()

    def test_error_FSC(self):
        with mock.patch(
            _FSC_provider_class + "._obtain_rates",
            return_value=None,
        ):
            self.fsc_provider._update(self.today, self.today)

    def test_update_FSC_today(self):
        """No checks are made since today may not be a banking day"""
        self.fsc_provider._update(self.today, self.today)
        self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ]
        ).unlink()

    def test_update_FSC_month(self):
        self.fsc_provider._update(self.today - relativedelta(months=1), self.today)

        rates = self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ],
            limit=1,
        )
        self.assertTrue(rates)

        self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ]
        ).unlink()

    def test_update_FSC_year(self):
        self.fsc_provider._update(self.today - relativedelta(years=1), self.today)

        rates = self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ],
            limit=1,
        )
        self.assertTrue(rates)

        self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ]
        ).unlink()

    def test_update_FSC_scheduled(self):
        self.fsc_provider.interval_type = "days"
        self.fsc_provider.interval_number = 14
        self.fsc_provider.next_run = self.today - relativedelta(days=1)
        self.fsc_provider._scheduled_update()

        rates = self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ],
            limit=1,
        )
        self.assertTrue(rates)

        self.CurrencyRate.search(
            [
                ("currency_id", "=", self.usd_currency.id),
            ]
        ).unlink()

    def test_update_FSC_no_base_update(self):
        self.fsc_provider.interval_type = "days"
        self.fsc_provider.interval_number = 14
        self.fsc_provider.next_run = self.today - relativedelta(days=1)
        self.fsc_provider._scheduled_update()

        rates = self.CurrencyRate.search(
            [
                ("company_id", "=", self.company.id),
                (
                    "currency_id",
                    "in",
                    [
                        self.usd_currency.id,
                        self.cop_currency.id,
                    ],
                ),
            ],
            limit=1,
        )
        self.assertTrue(rates)

        self.CurrencyRate.search(
            [
                ("company_id", "=", self.company.id),
            ]
        ).unlink()

    def test_update_FSC_sequence(self):
        self.fsc_provider.interval_type = "days"
        self.fsc_provider.interval_number = 1
        self.fsc_provider.last_successful_run = None
        self.fsc_provider.next_run = date(2019, 4, 1)

        self.fsc_provider._scheduled_update()
        self.assertEqual(self.fsc_provider.last_successful_run, date(2019, 4, 1))
        self.assertEqual(self.fsc_provider.next_run, date(2019, 4, 2))
        rates = self.CurrencyRate.search(
            [
                ("company_id", "=", self.company.id),
                ("currency_id", "=", self.usd_currency.id),
            ]
        )
        self.assertEqual(len(rates), 1)

        self.fsc_provider._scheduled_update()
        self.assertEqual(self.fsc_provider.last_successful_run, date(2019, 4, 2))
        self.assertEqual(self.fsc_provider.next_run, date(2019, 4, 3))
        rates = self.CurrencyRate.search(
            [
                ("company_id", "=", self.company.id),
                ("currency_id", "=", self.usd_currency.id),
            ]
        )
        self.assertEqual(len(rates), 2)

        self.CurrencyRate.search(
            [
                ("company_id", "=", self.company.id),
            ]
        ).unlink()

    def test_update_FSC_weekend(self):
        self.fsc_provider.interval_type = "days"
        self.fsc_provider.interval_number = 1
        self.fsc_provider.last_successful_run = None
        self.fsc_provider.next_run = date(2019, 7, 1)

        self.fsc_provider._scheduled_update()
        self.fsc_provider._scheduled_update()
        self.fsc_provider._scheduled_update()
        self.fsc_provider._scheduled_update()
        self.fsc_provider._scheduled_update()

        self.assertEqual(self.fsc_provider.last_successful_run, date(2019, 7, 5))
        self.assertEqual(self.fsc_provider.next_run, date(2019, 7, 6))

        self.fsc_provider._scheduled_update()
        self.fsc_provider._scheduled_update()

        self.assertEqual(self.fsc_provider.last_successful_run, date(2019, 7, 7))
        self.assertEqual(self.fsc_provider.next_run, date(2019, 7, 8))

    def test_foreign_base_currency(self):
        self.company.currency_id = self.chf_currency
        self.test_update_FSC_today()
        self.test_update_FSC_month()
        self.test_update_FSC_year()
        self.test_update_FSC_scheduled()
        self.test_update_FSC_no_base_update()
        self.test_update_FSC_sequence()
        self.test_update_FSC_weekend()
        self.company.currency_id = self.cop_currency
