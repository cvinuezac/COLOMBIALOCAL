# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import models, fields


class ResCity(models.Model):
    _inherit = "res.city"
    phone_prefix = fields.Char(string='Phone Prefix')
    code = fields.Char(string='City Code',
                       size=64,
                       help="The official code for the city")