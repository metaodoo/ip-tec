# -*- coding: utf-8 -*-

{
    'name': 'Website - WhatsApp Button',
    'version': '19.0.1.0',
    'license': 'OPL-1',
    'category': 'Website',
    'summary': 'Website - WhatsApp Button',
    'description': """Website - WhatsApp Button""",
    'author': 'Waleed Mohsen',
    'depends': ['portal', 'website'],
    'data': [
        'views/template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'wm_website_whatsapp_button/static/src/css/whatsapp.css',
        ],
    },
    'installable': True,
    'application': False,
}
