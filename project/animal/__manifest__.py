# Part of Intesco. See LICENSE file for full copyright and licensing details.


{
    "name": "Animal",
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
        "base",


        # Customize Module
    ],
    "data": [
        # Security


        # =============== DATA ===================
        # 'data/update_script_function.xml',
        # Master data
        # 'data/ir_config_parameter_data.xml',
        #    'data/ir_cron_data.xml',
        #    'data/mail_template_data.xml',
        #    'data/ir_config_parameter_data.xml',


        # =============== SECURITY ===============
        'security/ir.model.access.csv',
        'views/animal_view.xml',
        # =============== VIEWS ==================
        # Template

        # 'views/assets.xml',
        # Base
        # Application
        #    'views/hr_employee_view.xml',
        # =============== WIZARDS ================


        # =============== MENU ===================
        # 'menu/menu.xml',
        # =============== REPORT =================
    ],
    "qweb": [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
