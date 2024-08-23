# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import models, fields, api


class ResCountry(models.Model):
    _inherit = "res.country"

    name_dian = fields.Char(string="DIAN Name")
    name_iso = fields.Char(string="ISO Name")
    description = fields.Char(string="Description")
    code_alpha3 = fields.Char(string="Alpha Code 3", size=3)
    code_numeric = fields.Char(string="Numeric Code", size=3)
    code_dian = fields.Char(string="DIAN Code", size=3)

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []

        if name:
            args = [
                "|",
                "|",
                "|",
                "|",
                ("name", operator, name),
                ("name_dian", operator, name),
                ("name_iso", operator, name),
                ("code", operator, name),
                ("code_dian", operator, name),
            ] + args

        return self.search(args, limit=limit).name_get()

    @api.multi
    def name_get(self):
        res = []

        for record in self:
            name = "%s [%s]" % (record.name or "", record.code or "")
            res.append((record.id, name))

        return res
