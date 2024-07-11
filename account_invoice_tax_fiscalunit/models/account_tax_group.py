# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class AccountTaxGroup(models.Model):
    _inherit = "account.tax.group"

    fiscalunit_factor = fields.Float(
        string="Fiscal Unit Factor",
        help="Number of Fiscal Units from which the tax is calculated",
        digits=dp.get_precision("Fiscal Unit"))
