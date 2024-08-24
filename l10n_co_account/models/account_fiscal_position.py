# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    company_type = fields.Selection(
        string="Company Type",
        selection=[("person", "Natural Person"), ("company", "Juridical Person")],
    )
