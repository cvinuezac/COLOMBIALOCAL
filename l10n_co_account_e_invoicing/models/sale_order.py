# -*- coding: utf-8 -*-
# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    receipt_document_reference = fields.Char(
        string="Merchandise / Service Receipt Document", copy=False
    )

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({"receipt_document_reference": self.receipt_document_reference})

        return res
