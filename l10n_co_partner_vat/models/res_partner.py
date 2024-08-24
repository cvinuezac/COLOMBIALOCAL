# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    document_type_id = fields.Many2one(
        string="Document Type", comodel_name="res.partner.document.type"
    )
    document_type_code = fields.Char(related="document_type_id.code", store=False)
    check_digit = fields.Char(string="Verification Digit", size=1)
    identification_document = fields.Char(string="Identification Document")
