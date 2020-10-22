# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'students'
    _description = 'Tabla para registrar alumnos'

    name = fields.Char(String='Name of student')
    last_name = fields.Char(String='Last name')
    gender = fields.Selection([
        ('masculino','Masculino'),
        ('femenino', 'Femenino')
    ])
    age = fields.Integer(string="Age")