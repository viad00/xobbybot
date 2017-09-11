#!/bin/python2
# coding=UTF-8

from bot_session import repair_write_answer, unblock_user, block_user

ask_for_parts = u'Пиши "заказ" если нужны запчасти, "запись" - если все уже готово, "отмена" - если ты передумал'


def repair_answer(user_id, answer):
    repair_write_answer(user_id, answer)
    unblock_user(user_id)
    block_user(user_id, 'repair_type')
    return u'Ты уже купил запчасти или нам подобрать все необходимое для обслуживания?\n' + ask_for_parts, ''


def repair_type(user_id, answer):
    # TODO: Закончить второй этап
    if answer == u'заказ':
        return u'Заказ', ''
    elif answer == u'запись':
        return u'Запись', ''
    elif answer == u'отмена':
        return u'Отмена', ''
    else:
        return u'Прости я не понял\n' + ask_for_parts, ''