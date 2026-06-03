# -*- coding: utf-8 -*-
# from odoo import http


# class MetaWebFloatingSocialIcon(http.Controller):
#     @http.route('/meta_web_floating_social_icon/meta_web_floating_social_icon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meta_web_floating_social_icon/meta_web_floating_social_icon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('meta_web_floating_social_icon.listing', {
#             'root': '/meta_web_floating_social_icon/meta_web_floating_social_icon',
#             'objects': http.request.env['meta_web_floating_social_icon.meta_web_floating_social_icon'].search([]),
#         })

#     @http.route('/meta_web_floating_social_icon/meta_web_floating_social_icon/objects/<model("meta_web_floating_social_icon.meta_web_floating_social_icon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meta_web_floating_social_icon.object', {
#             'object': obj
#         })
