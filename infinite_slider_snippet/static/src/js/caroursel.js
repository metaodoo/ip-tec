/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.get_dashbaord_carousel = publicWidget.Widget.extend({
    selector: '.s_carousel_template',
    
    init: function() {
        this._super.apply(this, arguments);
    },
    
    start: function() {
        const self = this;
        
        rpc('/get_dashbaord_carousel', {}).then(function (data) {
            if (data) {
                self.$target.empty().append(data);
            }
        });
        
        rpc('/get_dashbaord_carousel_count', {}).then(function (data) {
            if (data) {
                document.querySelector(':root').style.setProperty('--image-count', data);
                document.querySelector(':root').style.setProperty('--image-speed', '22s');
            }
        });
        
        return this._super.apply(this, arguments);
    }
});
