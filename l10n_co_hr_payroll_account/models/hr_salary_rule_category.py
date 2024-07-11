# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).
from odoo import fields, models


class hrSalaryRuleCategory(models.Model):
    _inherit = 'hr.salary.rule.category'

    type = fields.Selection(selection=[('Devengado', 'Devengado'),
                                       ('Deducción', 'Deducción')],
                            string='Type')
