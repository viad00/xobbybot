# coding=UTF-8

import command_system
from bot_session import block_user


def tools(user_id):
    message = u'Отлично! Расскажи мне какие товары ты хочешь приобрести. Для подбора масла, фильтров или АКБ ' \
              u'обязательно укажи марку/модель автомобиля, гос.номер и VIN.'
    block_user(user_id, 'tools')
    return message, ''


info_command = command_system.Command()

info_command.keys = [u'заказ', u'купить интструменты', u'сделать заказ', u'tools', u'купить масло', u'order']
info_command.description = u'Закажу масло, автокосметику, инструмент и прочее'
info_command.process = tools
