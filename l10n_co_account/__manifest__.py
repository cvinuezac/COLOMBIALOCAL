# -*- coding: utf-8 -*-
# Copyright 2024 Joan Marín <Github@JoanMarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Colombian Localization Account",
    "version": "12.0.1.0.0",
    "category": "Localization",
    "author": "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-colombia",
    "depends": [
        "l10n_co",
        "account_debitnote",
        "account_invoice_refund_reason",
    ],
    "data": [
        "data/account.invoice.refund.reason.csv",
        "security/res_groups.xml",
        "views/account_invoice_refund_reason_views.xml",
        "views/account_invoice_views.xml",
        "views/account_journal_views.xml",
        "wizards/account_invoice_debitnote_views.xml",
        "wizards/account_invoice_refund_views.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
