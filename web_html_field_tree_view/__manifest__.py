# -*- coding: utf-8 -*-
# © 2018 Robert J Sullivan
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'HTML Field in Tree View',
    'category': 'Web',
    'author': 'Robert J Sullivan',
    'license': 'AGPL-3',
    'version': '10.0.1.0.0',
    'website': 'http://www.maxitmail.com',
    'summary': 'Column extension to properly display html data in a tree view.\nAdapted from https://stackoverflow.com/questions/45102334/display-html-in-tree-view-odoo.',
    'installable': True,
    'depends': [
        'web',
    ],
    'js': [
        'static/src/js/web_html_field_tree_view.js',
    ],
    'data': [
        'views/web_html_field_tree_view_assets.xml',
    ],
}
