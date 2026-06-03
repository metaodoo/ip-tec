# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class meta_web_floating_social_icon(models.Model):
#     _name = 'meta_web_floating_social_icon.meta_web_floating_social_icon'
#     _description = 'meta_web_floating_social_icon.meta_web_floating_social_icon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
