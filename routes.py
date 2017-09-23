# coding=UTF-8
import dialogs.block, dialogs.repair, dialogs.parts, dialogs.sales, dialogs.tools, dialogs.tyres, dialogs.admin

routes = {
    'unblock': dialogs.block.unblock,
    'repair': dialogs.repair.repair_answer,
    'repair_type': dialogs.repair.repair_type,
    'repair_ok': dialogs.repair.repair_ok,
    'parts': dialogs.parts.parts_answer,
    'parts_check': dialogs.parts.parts_check,
    'parts_bosch': dialogs.parts.parts_bosch,
    'sale_get': dialogs.sales.get_sale,
    'tools': dialogs.tools.tools_write,
    'tyres_size': dialogs.tyres.write_query,
    'tyres_season': dialogs.tyres.find_tyres,
    'tyres_dialog': dialogs.tyres.dialog_final,
    'tyres_order': dialogs.tyres.order,
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
}