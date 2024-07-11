# Copyright 2019 Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class UomCode(models.Model):
    _name = 'uom.code'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
