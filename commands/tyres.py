# coding=UTF-8

import command_system
from bot_session import block_user


def tyres(user_id):
    message = u'Подобрать диски тебе поможет консультант на месте (слишком много вариантов). ' \
                    u'А вот цены на шины я могу рассказать тебе если ты знаешь размер. ' \
                    u'Пиши размер в формате "195/65/15"'
    block_user(user_id, 'tyres_size')
    return message, ''


info_command = command_system.Command()

info_command.keys = [u'шины', u'заказать шины', u'tyre', u'tire']
info_command.description = u'Расскажу цены и закажу шины/диски.'
info_command.process = tyres
