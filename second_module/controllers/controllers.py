# -*- coding: utf-8 -*-
from odoo import http


class SecondModule(http.Controller):
     @http.route('/second_module/second_module', auth='public')
     def index(self, **kw):
         return "Hola Gabriel"

#     @http.route('/second_module/second_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('second_module.listing', {
#             'root': '/second_module/second_module',
#             'objects': http.request.env['second_module.second_module'].search([]),
#         })

#     @http.route('/second_module/second_module/objects/<model("second_module.second_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('second_module.object', {
#             'object': obj
#         })
