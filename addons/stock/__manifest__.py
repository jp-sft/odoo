# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inventory',
    'version': '1.1',
    'summary': 'Manage your stock and logistics activities',
    'description': "",
    'website': 'https://www.odoo.com/page/warehouse',
    'depends': ['product', 'barcodes', 'digest'],
    'category': 'Inventory/Inventory',
    'sequence': 25,
    'demo': [
        'data/stock_demo_pre.xml',
        'data/stock_demo.xml',
        'data/stock_demo2.xml',
        'data/stock_orderpoint_demo.xml',
        'data/stock_storage_category_demo.xml',
    ],
    'data': [
        'security/stock_security.xml',
        'security/ir.model.access.csv',

        'data/digest_data.xml',
        'data/mail_templates.xml',
        'data/default_barcode_patterns.xml',
        'data/stock_data.xml',
        'data/stock_sequence_data.xml',
        'data/stock_traceability_report_data.xml',

        'report/report_stock_forecasted.xml',
        'report/report_stock_quantity.xml',
        'report/stock_report_views.xml',
        'report/report_package_barcode.xml',
        'report/report_lot_barcode.xml',
        'report/report_location_barcode.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_deliveryslip.xml',
        'report/report_stockinventory.xml',
        'report/report_stock_rule.xml',
        'report/package_templates.xml',
        'report/picking_templates.xml',
        'report/product_templates.xml',
        'report/product_packaging.xml',
        'data/mail_template_data.xml',

        'views/stock_menu_views.xml',
        'wizard/stock_assign_serial_views.xml',
        'wizard/stock_change_product_qty_views.xml',
        'wizard/stock_picking_return_views.xml',
        'wizard/stock_scheduler_compute_views.xml',
        'wizard/stock_immediate_transfer_views.xml',
        'wizard/stock_inventory_conflict.xml',
        'wizard/stock_backorder_confirmation_views.xml',
        'wizard/stock_quantity_history.xml',
        'wizard/stock_request_count.xml',
        'wizard/stock_rules_report_views.xml',
        'wizard/stock_warn_insufficient_qty_views.xml',
        'wizard/product_replenish_views.xml',
        'wizard/stock_track_confirmation_views.xml',
        'wizard/stock_orderpoint_snooze_views.xml',
        'wizard/stock_package_destination_views.xml',

        'views/res_partner_views.xml',
        'views/product_strategy_views.xml',
        'views/product_views.xml',
        'views/stock_production_lot_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_scrap_views.xml',
        'views/stock_quant_views.xml',
        'views/stock_location_views.xml',
        'views/stock_warehouse_views.xml',
        'views/stock_move_line_views.xml',
        'views/stock_move_views.xml',
        'views/stock_orderpoint_views.xml',
        'views/stock_storage_category_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_stock_traceability.xml',
        'views/stock_template.xml',
        'views/stock_rule_views.xml',
        'views/stock_package_level_views.xml',
        'views/stock_package_type_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': '_assign_default_mail_template_picking_id',
    'assets': {
        'web.report_assets_common': [
            'web/static/src/scss/views.scss',
            'web/static/src/scss/graph_view.scss',
            'stock/static/src/scss/report_stock_forecasted.scss',
            'stock/static/src/scss/report_stock_rule.scss',
        ],
        'web.assets_common': [
            'stock/static/src/scss/stock_traceability_report.scss',
        ],
        'web.assets_backend': [
            'stock/static/src/js/inventory_report_list_controller.js',
            'stock/static/src/js/inventory_report_list_view.js',
            'stock/static/src/js/inventory_singleton_list_renderer.js',
            'stock/static/src/js/inventory_singleton_list_controller.js',
            'stock/static/src/js/inventory_singleton_list_view.js',
            'stock/static/src/js/report_stock_forecasted.js',
            'stock/static/src/js/stock_orderpoint_list_controller.js',
            'stock/static/src/js/stock_orderpoint_list_model.js',
            'stock/static/src/js/stock_orderpoint_list_view.js',
            'stock/static/src/js/stock_traceability_report_backend.js',
            'stock/static/src/js/stock_traceability_report_widgets.js',
            'stock/static/src/js/popover_widget.js',
            'stock/static/src/js/forecast_widget.js',
            'stock/static/src/js/basic_model.js',
            'stock/static/src/js/stock_rescheduling_popover.js',
            'stock/static/tests/tours/stock_report_tests.js',
            'stock/static/src/scss/forecast_widget.scss',
            'stock/static/src/scss/stock_traceability_report.scss',
            'stock/static/src/scss/stock_empty_screen.scss',
        ],
        'web.qunit_suite_tests': [
            'stock/static/tests/singleton_list_tests.js',
            'stock/static/tests/popover_widget_tests.js',
            'stock/static/tests/stock_traceability_report_backend_tests.js',
        ],
        'web.assets_qweb': [
            'stock/static/src/xml/inventory_report.xml',
            'stock/static/src/xml/inventory_lines.xml',
            'stock/static/src/xml/popover_widget.xml',
            'stock/static/src/xml/forecast_widget.xml',
            'stock/static/src/xml/report_stock_forecasted.xml',
            'stock/static/src/xml/stock_orderpoint.xml',
            'stock/static/src/xml/stock_traceability_report_backend.xml',
        ],
    },
    'license': 'LGPL-3',
}
