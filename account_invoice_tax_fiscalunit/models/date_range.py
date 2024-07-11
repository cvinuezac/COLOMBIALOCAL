# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class DateRange(models.Model):
    _inherit = 'date.range'

    fiscalunit = fields.Float(string='Fiscal Unit',
                              help='Value of Fiscal Unit as the Colombian UVT',
                              digits=dp.get_precision('Fiscal Unit'))
