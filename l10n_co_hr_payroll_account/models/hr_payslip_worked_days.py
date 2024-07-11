# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).
from odoo import models, fields


class HrPayslipWorkedDays(models.Model):
    _name = "hr.payslip.worked_days"
    _inherit = "hr.payslip.worked_days"

    holiday_id = fields.Many2one(comodel_name='hr.holidays', string='Absence')
