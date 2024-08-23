# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0).

{
    "name": "Colombian Data ZIP/Cities, States and Countries",
    "version": "12.0.1.0.0",
    "category": "Localization",
    "author": "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Odoo Community Association (OCA)",
    "maintainers": ["joanmarin"],
    "website": "https://github.com/OCA/l10n-colombia",
    "depends": [
        "base_location",
    ],
    "data": [
        "data/res.country.csv",
        "data/res.country.state.csv",
        "data/res.city.csv",
        "data/res.city.zip.csv",
        "views/res_city_views.xml",
        "views/res_city_zip_views.xml",
        "views/res_country_state_views.xml",
        "views/res_country_views.xml",
        "views/res_partner_views.xml"
    ],
    "installable": True,
    "license": "AGPL-3",
}
