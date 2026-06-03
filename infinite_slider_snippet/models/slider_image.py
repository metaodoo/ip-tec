from odoo import models, fields, api, _

class SliderImage(models.Model):
    _name = 'slider.image'

    name = fields.Char(string="Name")
    lnk=fields.Char(string="Url",default="/")#added by rifat
    image = fields.Binary(string='Image', attachment=True)
    img_url=fields.Char(string='Image URL',compute="get_img_url")
    
    def get_img_url(self):
        for rec in self:
            rec.img_url=f"web/content/?model=slider.image&id={str(rec.id)}&filename_field=name&field=image&filename={rec.name}"