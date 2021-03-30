# -*- coding: utf-8 -*
# from odoo import http


# class CmDemo(http.Controller):
#     @http.route('/cm_demo/cm_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cm_demo/cm_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cm_demo.listing', {
#             'root': '/cm_demo/cm_demo',
#             'objects': http.request.env['cm_demo.cm_demo'].search([]),
#         })

#     @http.route('/cm_demo/cm_demo/objects/<model("cm_demo.cm_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cm_demo.object', {
#             'object': obj
#         })
