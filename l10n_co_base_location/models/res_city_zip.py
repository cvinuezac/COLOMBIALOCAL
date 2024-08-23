# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import models, fields


class ResCityZip(models.Model):
    _inherit = "res.city.zip"

    city_code = fields.Char(string="City Code", size=5, related="city_id.code")
    phone_code = fields.Char(string="Calling Code", related="city_id.phone_code")
    type = fields.Selection(
        selection=[("urban", "Urban"), ("rural", "Rural")], string="Type"
    )
