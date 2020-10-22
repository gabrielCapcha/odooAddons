# -*- coding: utf-8 -*-

from odoo import models, fields, api


class third_module(models.Model):
     _name = 'third_module.third_module'
     _description = 'third_module.third_module'

     name = fields.Char()
     number = fields.Integer()
     float_number = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
