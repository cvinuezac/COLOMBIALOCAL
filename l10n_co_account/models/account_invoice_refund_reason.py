# -*- coding: utf-8 -*-
# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceRefundReason(models.Model):
    _inherit = "account.invoice.refund.reason"
    _order = "code ASC"

    name = fields.Char(string="Name", required=True, translate=False)
    code = fields.Char(string="Code")
    type = fields.Selection(
        selection=[("credit", "Credit Note"), ("debit", "Debit Note")], string="Type"
    )
