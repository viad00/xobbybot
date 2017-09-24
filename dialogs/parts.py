#!/bin/python2
# coding=UTF-8

from bot_session import block_user, unblock_user, parts_write_answer, parts_update_type, parts_remove_query, parts_get_text
import mail_sender

ask_for_parts = u'Пиши "запись" - если хочешь записаться на сервис, \n"заказ" - если не требуется установка' \
                u', \n"отмена" - если ты передумал'
refuse = u'Вы отменили заказ.\nЕсли вы хотите записаться ещё раз, то напишите "запчасти".\n' \
               u'Если вам нужна помощь то напишите "помощь".'
exit_mode = u'Отлично! Через некторое время с тобой свяжется менеджер. Если у тебя остались вопросы, пиши "помощь". ' \
            u'Кстати, у нас действуют акции. Хочешь узнать как получить бонус? Пиши "акции".'
bosch = u'Хочешь чтобы специалисты BOSCH Car Service установили детали на нашей СТО?\n'


def parts_answer(user_id, answer):
    parts_write_answer(user_id, answer)
    unblock_user(user_id)
    block_user(user_id, 'parts_check')
    return u'Проверь правильно ли указан VIN машины. ОТ этого будет зависеть скорость и точность подбора деталей.\n' \
           u'Если все верно, пиши "ок". \nЕсли есть ошибка - "отмена" и введи корректные данные сначала.', ''


def parts_check(user_id, answer):
    if answer == u'ok' or answer == u'ок':
        unblock_user(user_id)
        block_user(user_id, 'parts_bosch')
        return bosch + ask_for_parts, ''
    elif answer == u'отмена':
        parts_remove_query(user_id)
        unblock_user(user_id)
        return refuse, ''
    else:
        return u'Прости я не понял.\n' \
               u'Если все верно, пиши "ок". \nЕсли есть ошибка - "отмена" и введи корректные данные сначала.', ''


def parts_bosch(user_id, answer):
    if answer == u'заказ':
        unblock_user(user_id)
        parts_update_type(user_id, u'заказ')
        mail_sender.send_mail(parts_get_text(user_id), user_id, u'Заказ запчастей')
        return exit_mode, ''
    elif answer == u'запись':
        unblock_user(user_id)
        parts_update_type(user_id, u'запись')
        mail_sender.send_mail(parts_get_text(user_id), user_id, u'Запись на устаноку и заказ запчастей')
        return exit_mode, ''
    elif answer == u'отмена':
        parts_remove_query(user_id)
        unblock_user(user_id)
        return refuse, ''
    else:
        return u'Прости я не понял.\n' + ask_for_parts, ''
