# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    fiscal_responsibility_ids = fields.Many2many(
        comodel_name="account.fiscal.responsibility",
        relation="account_fiscal_position_responsibility_rel",
        column1="fiscal_position_id",
        column2="fiscal_responsibility_id",
        string="Fiscal Responsibilities",
        required=True,
    )
    tax_detail = fields.Selection(
        selection=[
            ("01", "IVA"),
            ("04", "INC"),
            ("ZA", "IVA e INC"),
            ("ZZ", "No aplica"),
        ],
        string="Tax Detail",
    )
    company_type = fields.Selection(
        selection=[("person", "Natural Person"), ("company", "Juridical Person")],
        string="Company Type",
    )
