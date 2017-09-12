#!/bin/python2
# coding=UTF-8

from bot_session import repair_write_answer, unblock_user, block_user, repair_remove_query, repair_update_type

ask_for_parts = u'Пиши \n"заказ" если нужны запчасти, \n"запись" - если все уже готово, \n"отмена" - если ты передумал'
refuse = u'Вы отменили запись на ремонт.\nЕсли вы хотите записаться ещё раз, то напишите "ремонт".\n' \
               u'Если вам нужна помощь то напишите "помощь".'
exit_mode = u'Отлично! Через некторое время с тобой свяжется менеджер для огласования даты и времени твоего ' \
               u'ремонта. Если у тебя остались вопросы, пиши "помощь". Кстати, у нас действуют акции. Хочешь узнать ' \
               u'как получить бонус? Пиши "акции".'  # Если у тебя больше нет вопросов, пиши "выход".'


def repair_answer(user_id, answer):
    repair_write_answer(user_id, answer)
    unblock_user(user_id)
    block_user(user_id, 'repair_type')
    return u'Ты уже купил запчасти или нам подобрать все необходимое для обслуживания?\n' + ask_for_parts, ''


def repair_type(user_id, answer):
    if answer == u'заказ':
        repair_update_type(user_id, u'заказ')
        unblock_user(user_id)
        block_user(user_id, 'repair_ok')
        return u'Проверь правильно ли указан VIN машины. От этого будет зависеть скорость и точность подбора деталей. ' \
               u'Если все верно, пиши "ок".\nЕсли есть ошибка пиши "отмена" и введи корректные данные сначала', ''
    elif answer == u'запись':
        repair_update_type(user_id, u'запись')
        unblock_user(user_id)
        return exit_mode, ''
    elif answer == u'отмена':
        unblock_user(user_id)
        repair_remove_query(user_id)
        return refuse, ''
    else:
        return u'Прости я не понял\n' + ask_for_parts, ''


def repair_ok(user_id, answer):
    if answer == u'ок' or answer == u'ok':
        unblock_user(user_id)
        return exit_mode, ''
    elif answer == u'отмена':
        repair_remove_query(user_id)
        unblock_user(user_id)
        return refuse, ''
    else:
        return u'Прости я не понял\n' + u'Если все верно, пиши "ок".\nЕсли есть ошибка пиши "отмена" и введи корректные' \
                                        u' данные сначала', ''
