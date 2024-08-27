# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class AccountFiscalResponsibility(models.Model):
    _name = "account.fiscal.responsibility"
    _description = "Fiscal Responsibilities"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
