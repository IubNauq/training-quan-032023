# -*- coding: utf-8 -*-
from odoo import fields, models


class MyPet(models.Model):
    _name = "my.pet"
    _description = "My Pet"

    name = fields.Char(string='Pet Name', required=True)
    # nickname = fields.Char('Nickname')
    # description = fields.Text('Pet Description')
    # age = fields.Integer('Pet Age', default=1)
    # weight = fields.Float('Weight (kg)')
    # dob = fields.Date('DOB', required=False)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # ], string='Gender', default='male')
    # pet_image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    # owner_id = fields.Many2one('res.partner', string='Owner')
    # product_ids = fields.Many2many(comodel_name='product.product',
    #                                string="Related Products",
    #                                relation='pet_product_rel',
    #                                column1='col_pet_id',
    #                                column2='col_product_id')
