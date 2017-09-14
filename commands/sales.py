# coding=UTF-8

import command_system
from bot_session import get_all_sales, block_user


def sales(user_id):
    message = u'В Хобби-Авто можно получить следующие бонусы:\n'
    all_sales = get_all_sales()
    for row in all_sales:
        message += str(row[0]) + u' - ' + row[1] + u'\n'
    message += u'Чтобы узнать подробнее об акции, введите её номер.\nПиши "выход" чтобы выйти из меню'
    block_user(user_id, 'sale_get')
    return message, ''

info_command = command_system.Command()

info_command.keys = [u'акции', u'скидки', u'бонусы', u'sales']
info_command.description = u'Покажу акции, бонусы, скидки'
info_command.process = sales
