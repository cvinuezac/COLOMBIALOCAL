# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class UomUom(models.Model):
    _inherit = "uom.uom"

    code = fields.Char(string="Code", size=3, required=True)
