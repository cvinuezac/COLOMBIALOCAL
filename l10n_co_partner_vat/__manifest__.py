# Copyright 2018 Joan Marín <Github@JoanMarin>
# Copyright 2018 Guillermo Montoya <Github@guillermm>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

{
    "name":
    "Partner VAT Colombia",
    "summary":
    "Module for Type of Identification Document and Colombian NIT Checking.",
    "version":
    "12.0.1.0.0",
    "license":
    "AGPL-3",
    "website":
    "https://github.com/exaap/l10n-colombia",
    "author":
    "EXA Auto Parts Github@exaap, "
    "Alejandro Olano Github@alejo-code, "
    "Joan Marín Github@JoanMarin, "
    "Guillermo Montoya Github@guillermm",
    "category":
    "Localization",
    "depends": ["base_vat", "account"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_partner_document_type_data.xml",
        "views/res_partner_views.xml"
    ],
    "installable":
    True,
}
