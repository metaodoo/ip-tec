# -*- coding: utf-8 -*-
{
    'name': "Meta Website Floating Social Icon",

    'summary': """
        Floating Social Icons for website side bar""",

    'description': """
        Floating Social Icons for website side bar
    """,

    'author': "Metamorphosis, Rifat Anwar",
    'co-author': "Rifat Anwar",
    'website': "https://metamorphosis.com.bd",
    'category': 'Website',
    'version': '19.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/social_floating_icon.xml',
        'views/views.xml',
    ],
    
    'assets':{
        
        'web.assets_frontend':[
            'meta_web_floating_social_icon/static/src/scss/social_floating_icon.scss',
            
        ],
        
    },
    
    'sequence':0,
    'application':True,
    'installable':True,
    'auto-install':False
}
