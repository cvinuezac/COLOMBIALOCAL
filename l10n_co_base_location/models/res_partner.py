# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

from odoo import api, models, fields, _
from lxml import etree


class ResPartner(models.Model):
    _inherit = "res.partner"

    country_code = fields.Char(related="country_id.code", store=False)

    @api.model
    def _fields_view_get_address(self, arch):
        arch = super(ResPartner, self)._fields_view_get_address(arch)
        # render the partner address accordingly to address_view_id
        doc = etree.fromstring(arch)
        replacement_xml = """
            <div>
                <field name="country_code" invisible="1"/>
                <field name="city" placeholder="%(placeholder)s" class="o_address_city"
                    attrs="{
                        'invisible': [('country_enforce_cities', '=', True), ('city_id', '!=', False)],
                        'readonly': [('type', '=', 'contact')%(parent_condition)s],
                        'required': [('country_code', '!=', 'CO'), ('supplier', '=', True)]
                    }"
                />
            </div>
        """
        replacement_data = {
            "placeholder": _("City"),
        }

        def _arch_location(node):
            in_subview = False
            view_type = False
            parent = node.getparent()

            while parent is not None and (not view_type or not in_subview):
                if parent.tag == "field":
                    in_subview = True
                elif parent.tag in ["list", "tree", "kanban", "form"]:
                    view_type = parent.tag

                parent = parent.getparent()

            return {"view_type": view_type, "in_subview": in_subview}

        for city_node in doc.xpath("//field[@name='city']"):
            location = _arch_location(city_node)
            replacement_data["parent_condition"] = ""

            if location["view_type"] == "form" or not location["in_subview"]:
                replacement_data["parent_condition"] = ", ('parent_id', '!=', False)"

            replacement_formatted = replacement_xml % replacement_data

            for replace_node in etree.fromstring(replacement_formatted):
                # raise Warning(etree.tostring(city_node, encoding="unicode"), etree.tostring(replace_node, encoding="unicode"))
                city_node.addprevious(replace_node)

            parent = city_node.getparent()
            parent.remove(city_node)

        arch = etree.tostring(doc, encoding="unicode")

        return arch
