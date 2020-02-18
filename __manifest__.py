# -*- coding: utf-8 -*-
{
    'name': "Gestio Hospital",

    'summary': """Eina de gestio d'hospitals""",

    'description': """La eina pot gestionar diferents hospitals, a partir de:
        -Hospital
        -Pacient -> Historial -> Visita -> Malaltia
        -Persona
        -Metge
        -Adreça
    """,

    'author': "Cristofol Lluis Rivas I Thwaite",
    'website': "http://www.copernic.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
