# -*- coding: utf-8 -*-
{
    'name': "Expenditure Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        User story
        Là một thủ quỹ tôi muốn quản lý được thu, chi của Battech
        Là một thủ quỹ tôi muốn biết được danh sách các nhân viên trong Battech và số tiền phải đóng
        Là một thủ quỹ tôi muốn xem báo cáo thu chi trong tháng
        Là 1 thủ quyx tôi muốn tìm kiếm nhanh thu chi theo người, theo ngày tháng….
        Là 1 thủ quỹ tôi muốn nhắc nhở nhân viên khi chưa đóng quỹ( 10 hàng tháng) gửi email và dùng ir.cron
    """,

    'author': "Tinh Nguyen",
    'website': "www.facebook.com/tinhlionel229",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/staff_view.xml',
        'views/position_rule_view.xml',
        'security/expenditure_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application':True,
}

