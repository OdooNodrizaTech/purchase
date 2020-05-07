# -*- coding: utf-8 -*-
{
    'name': 'Purchase Order Mail Followers Extra',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Delivery',
    'license': 'AGPL-3',
    'depends': ['base', 'purchase'],    
    'data': [
        'views/purchase_order_mail_followers_extra.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,    
}