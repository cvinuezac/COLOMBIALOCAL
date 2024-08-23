# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import models, fields


class ResCountryState(models.Model):
    _inherit = "res.country.state"

    phone_code = fields.Char(string='Calling Code')
