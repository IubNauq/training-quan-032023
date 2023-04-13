# Part of Intesco. See LICENSE file for full copyright and licensing details.


{
    "name": "Payroll Wage History",
    "version": "1.0",
    "description": """
       This module will tag assigner automatically after finishing a task of a
       project.
   """,
    "author": "Intesco Co.,LTD",
    "website": "https://ivf.com.vn",
    'category': "Module",
    "depends": [


        # Native Odoo
        "base", "hr"


        # Customize Module
    ],
    "data": [
        # =============== DATA ===================
        'data/payroll_wage_history_data.xml',


        # =============== SECURITY ===============
        'security/ir.model.access.csv',
        'security/payroll_wage_history_security.xml',

        # =============== VIEWS ==================
        'views/payroll_view.xml',
        'views/menu_item.xml',
        'views/hr_employee.xml',

        # =============== WIZARDS ================
        'wizards/wizard_payroll.xml',

        # =============== MENU ===================
        # 'menu/menu.xml',
        # =============== REPORT =================
        'reports/report_payroll.xml',
        'reports/report.xml'


    ],
    "qweb": [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
