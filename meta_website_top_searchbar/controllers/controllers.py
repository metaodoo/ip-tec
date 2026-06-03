# -*- coding: utf-8 -*-
# from odoo import http


# class MetaWebsiteTopSearchbar(http.Controller):
#     @http.route('/meta_website_top_searchbar/meta_website_top_searchbar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meta_website_top_searchbar/meta_website_top_searchbar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('meta_website_top_searchbar.listing', {
#             'root': '/meta_website_top_searchbar/meta_website_top_searchbar',
#             'objects': http.request.env['meta_website_top_searchbar.meta_website_top_searchbar'].search([]),
#         })

#     @http.route('/meta_website_top_searchbar/meta_website_top_searchbar/objects/<model("meta_website_top_searchbar.meta_website_top_searchbar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meta_website_top_searchbar.object', {
#             'object': obj
#         })
