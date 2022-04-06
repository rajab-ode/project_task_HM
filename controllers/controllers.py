# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderTaskPakWiku(http.Controller):
#     @http.route('/sale_order_task_pak_wiku/sale_order_task_pak_wiku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_task_pak_wiku/sale_order_task_pak_wiku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_task_pak_wiku.listing', {
#             'root': '/sale_order_task_pak_wiku/sale_order_task_pak_wiku',
#             'objects': http.request.env['sale_order_task_pak_wiku.sale_order_task_pak_wiku'].search([]),
#         })

#     @http.route('/sale_order_task_pak_wiku/sale_order_task_pak_wiku/objects/<model("sale_order_task_pak_wiku.sale_order_task_pak_wiku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_task_pak_wiku.object', {
#             'object': obj
#         })
