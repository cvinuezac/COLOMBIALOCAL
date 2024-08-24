# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import api, fields, models


class L10nLatamIdentificationType(models.Model):
    _inherit = "l10n_latam.identification.type"

    code_dian = fields.Char("DIAN Code")

    @api.multi
    def name_get(self):
        res = []

        for record in self:
            name = "[%s] %s" % (record.code_dian, record.name)
            res.append((record.id, name))

        return res
