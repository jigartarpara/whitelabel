# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
        {
            "module_name": "Accounts",
            "type": "module",
            "label": _("Accounts 2"),
            "color": "blue",
            "icon": "khatavahi_icon/accounts-removebg-preview.png"
        },
        {
            "module_name": "Selling",
            "type": "module",
            "label": _("Selling 2"),
            "color": "green",
            "icon": "octicon octicon-tag"
        }

    ]
