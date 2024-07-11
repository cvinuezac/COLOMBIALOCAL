# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import models, fields, api


class AccountInvoiceRefund(models.TransientModel):
    _inherit = "account.invoice.refund"

    reason_id = fields.Many2one(
        comodel_name="account.invoice.refund.reason",
        string="Correction Concept",
        required=True,
        domain="[('type', '=', 'credit')]",
    )

    @api.multi
    def compute_refund(self, mode="refund"):
        res = super().compute_refund(mode)
        inv_obj = self.env["account.invoice"]
        context = dict(self._context or {})

        for inv in inv_obj.browse(context.get("active_ids")):
            inv.reason_id = False

        if isinstance(res["domain"], list):
            invoice_domain = []

            for domain in res["domain"]:
                if "type" not in domain:
                    invoice_domain.append(domain)

            invoice_id = inv_obj.search(invoice_domain)
            res["domain"] = invoice_domain

            if invoice_id:
                invoice_id.reason_id = self.reason_id.id

        return res
