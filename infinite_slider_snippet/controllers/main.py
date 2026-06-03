from odoo import http
from odoo.http import request
import logging

class DashbaordCarousel(http.Controller):
    @http.route('/get_dashbaord_carousel', auth="public", type='json')
    def get_dashbaord_carousel(self):
        records = request.env['slider.image'].sudo().search([])
        records_grouped = []
        records_data = [{'image_url': record.img_url, 'link': record.lnk} for record in records]
        
        for record in records:
            # img_url = "web/content/?model=slider.image&id=" + str(record.id) + "&filename_field=name&field=image&filename="+record.name
            records_grouped.append(record.img_url)
            
            # records_data.append({'image_url': record.img_url,'link': record.lnk})
            
        logging.info(f"Record Object Of Slider--------------->{records_grouped}")
        logging.info(f"Record Data of Slider--------------->{records_data}")
        
        # values = { "objects": records_grouped }
        values = {"objects": records_data}
        logging.info(f"Values For Qweb--------------->{values}")
        
        response = http.Response(template='infinite_slider_snippet.s_carousel_template_items', qcontext=values)
        logging.info(f"Response Data--------------->{response}")
        return response.render()

    @http.route('/get_dashbaord_carousel_count', auth="public", type='json')
    def get_dashbaord_carousel_count(self):
        records = request.env['slider.image'].sudo().search([])
        return len(records)