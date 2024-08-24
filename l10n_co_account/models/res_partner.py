# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    company_type = fields.Selection(
        selection=[("person", "Natural Person"), ("company", "Juridical Person")]
    )
    l10n_co_identification_type_code = fields.Char(
        related="l10n_latam_identification_type_id.code_dian", store=False
    )
    l10n_co_identification_document = fields.Char(string="Identification Document")
    l10n_co_verification_digit = fields.Char(string="Verification Digit", size=1)
    industry_id = fields.Many2one(domain="[('type', '!=', 'view')]")
    secondary_industry_ids = fields.Many2many(
        domain="[('id', '!=', industry_id), ('type', '!=', 'view')]"
    )

    @api.onchange(
        "country_id",
        "l10n_latam_identification_type_id",
        "l10n_co_identification_document",
        "l10n_co_verification_digit",
    )
    def _onchange_vat(self):
        if self.country_id and self.l10n_co_identification_document:
            if (
                self.l10n_co_verification_digit
                and self.l10n_co_identification_type_code == "31"
            ):
                self.vat = (
                    self.country_id.code
                    + self.l10n_co_identification_document
                    + self.l10n_co_verification_digit
                )
            elif self.l10n_co_identification_type_code == "43":
                self.l10n_co_verification_digit = False
                self.vat = "CO" + self.l10n_co_identification_document
            else:
                self.l10n_co_verification_digit = False
                self.vat = self.country_id.code + self.l10n_co_identification_document
        elif not self.l10n_co_identification_document and self.vat:
            self.vat = False

    def _compute_verification_digit(self):
        if not self.l10n_co_identification_document:
            return False

        prime = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
        identification_document = self.l10n_co_identification_document.strip()
        verification_digit = 0

        for i, character in enumerate(identification_document[::-1]):
            try:
                digit = int(character)
            except:
                return False

            verification_digit += digit * prime[i]

        verification_digit %= 11
        verification_digit = verification_digit if verification_digit >= 0 else 0

        return (
            (11 - verification_digit) if verification_digit >= 2 else verification_digit
        )
