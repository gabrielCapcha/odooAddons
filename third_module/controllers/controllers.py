# -*- coding: utf-8 -*-
from odoo import http


class ThirdModule(http.Controller):
     @http.route('/third_module/third_module/', auth='public')
     def index(self, **kw):
         return "Hello, third module"

#     @http.route('/third_module/third_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('third_module.listing', {
#             'root': '/third_module/third_module',
#             'objects': http.request.env['third_module.third_module'].search([]),
#         })

#     @http.route('/third_module/third_module/objects/<model("third_module.third_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('third_module.object', {
#             'object': obj
#         })
