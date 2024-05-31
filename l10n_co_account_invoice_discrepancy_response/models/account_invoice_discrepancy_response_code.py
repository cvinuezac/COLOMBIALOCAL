# -*- coding: utf-8 -*-
# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class AccountInvoiceDiscrepancyResponseCode(models.Model):
    _name = "account.invoice.discrepancy.response.code"
    _description = "Correction concept for Refund Invoice"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    type = fields.Selection(
        selection=[("credit", _("Credit Note")), ("debit", _("Debit Note"))],
        string="Type",
    )
