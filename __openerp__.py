{
    'name' : 'Custom pos ticket ',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Point Of Sale',
    'website' : 'https://yelizariev.github.io',
    'description': """
    module *ir_sequence_autoreset* is available here: https://github.com/yelizariev/addons-yelizariev
    """,
    'depends' : ['point_of_sale'],
    'data':[
        'data.xml',
        'views.xml',
        ],
    'js': [
        'static/lib/moment.js',
        'static/src/js/pos.js',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
    'auto_install': False,
}
