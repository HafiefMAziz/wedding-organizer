# -*- coding: utf-8 -*-
{
    'name': "wedding_organizer",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/stage_views.xml',
        'views/aisle_views.xml',
        'views/chair_views.xml',
        'views/guest_chair_views.xml',
        'views/order_views.xml',
        'views/staff_views.xml',
        'views/customer_views.xml',
        'views/returning_views.xml',
        'views/accounting_views.xml',
        # 'reports/report.xml',
        # 'reports/order_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
