# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    company_type = fields.Selection(
        selection=[("person", "Natural Person"), ("company", "Juridical Person")]
    )
    industry_id = fields.Many2one(domain="[('type', '!=', 'view')]")
    secondary_industry_ids = fields.Many2many(
        domain="[('id', '!=', industry_id), ('type', '!=', 'view')]"
    )
