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
        "base", "hr_contract"


        # Customize Module
    ],
    "data": [
        # =============== DATA ===================
        'data/payroll_wage_history_data.xml',

        # =============== SECURITY ===============
        'security/ir.model.access.csv',
        'security/payroll_wage_history_security.xml',

        # =============== VIEWS ==================
        'views/payroll_wage_history_views.xml',
        'views/hr_employee_views.xml',

        # =============== WIZARDS ================
        'wizards/wage_summary_wizard.xml',

        # =============== MENU ===================
        'menu/menu.xml',

        # =============== REPORT =================
        'reports/report_payroll.xml',
        'reports/report_employee_payroll.xml'


    ],
    "qweb": [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
