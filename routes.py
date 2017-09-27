# coding=UTF-8
import dialogs.block, dialogs.admin, dialogs.test

routes = {
    'unblock': dialogs.block.unblock,
    'admin_start': dialogs.admin.start,
    'admin_stock': dialogs.admin.stock,
    'admin_sales': dialogs.admin.sales,
    'admin_admin': dialogs.admin.admin,
    'admin_price': dialogs.admin.price,
    'admin_price_install': dialogs.admin.price_install,
    'admin_price_store':dialogs.admin.price_store,
    'admin_price_fix': dialogs.admin.price_fix,
    'admin_admin_add': dialogs.admin.admin_add,
    'admin_sale_add': dialogs.admin.add_sale,
    'admin_sale_add_p1': dialogs.admin.add_sale_p1,
    'test': dialogs.test.handler,
}