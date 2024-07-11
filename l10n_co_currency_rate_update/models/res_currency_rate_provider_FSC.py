# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from sodapy import Socrata
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class ResCurrencyRateProviderFSC(models.Model):
    _inherit = "res.currency.rate.provider"

    service = fields.Selection(
        selection_add=[("FSC", "Financial Superintendence of Colombia")],
        # ondelete={"FSC": "set default"}, Odoo 16.0
    )

    @api.model
    def _get_supported_currencies(self):
        self.ensure_one()
        if self.service == "FSC":
            # List of currencies obrained from:
            # https://dev.socrata.com/foundry/www.datos.gov.co/32sa-8pi3
            return ["USD"]

        return super()._get_supported_currencies()

    @api.model
    def _obtain_rates(self, base_currency, currencies, date_from, date_to):
        self.ensure_one()
        if self.service == "FSC":
            if base_currency != "COP":
                raise UserError(
                    _(
                        "Financial Superintendence of Colombia is suitable only"
                        " for companies with COP as base currency!"
                    )
                )

            data = {}

            for currencie in currencies:
                client = Socrata("www.datos.gov.co", None)
                results = []
                date = date_from

                while date <= date_to:
                    results += client.get("32sa-8pi3", where="vigenciadesde='%s'" % date)
                    date += relativedelta(days=1)

                for rate in results:
                    rate_date = fields.Date.from_string(
                        rate.get("vigenciadesde")
                    ).strftime(DEFAULT_SERVER_DATE_FORMAT)

                    if data.get(rate_date):
                        data[rate_date][currencie] = 1 / float(rate.get("valor"))
                    else:
                        rate_dict = {currencie: 1 / float(rate.get("valor"))}
                        data[rate_date] = rate_dict

            return data

        return super()._obtain_rates(base_currency, currencies, date_from, date_to)
