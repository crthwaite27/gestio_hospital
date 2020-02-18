# -*- coding: utf-8 -*-
from odoo import http

# class GestioHospital(http.Controller):
#     @http.route('/gestio_hospital/gestio_hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestio_hospital/gestio_hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestio_hospital.listing', {
#             'root': '/gestio_hospital/gestio_hospital',
#             'objects': http.request.env['gestio_hospital.gestio_hospital'].search([]),
#         })

#     @http.route('/gestio_hospital/gestio_hospital/objects/<model("gestio_hospital.gestio_hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestio_hospital.object', {
#             'object': obj
#         })