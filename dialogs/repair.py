#!/bin/python2
# coding=UTF-8

from bot_session import repair_write_answer

def repair_answer(user_id, answer):
    repair_write_answer(user_id, answer)
    return 'Ты уже купил запчасти или нам подобрать все необходимое для обслуживания?' \
           ' Пиши "заказ" если нужны запчасти. "Запись" - если все уже готово.', ''