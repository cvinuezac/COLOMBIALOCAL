# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    reason_id = fields.Many2one(
        comodel_name="account.invoice.refund.reason",
        string="Correction Concept",
        domain="[('type', 'in', {'out_invoice': ['debit'], 'out_refund': ['credit']}.get(type, []))]",
    )
