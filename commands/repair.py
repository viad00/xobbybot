# coding=UTF-8
import command_system
from bot_session import block_user


def info(user_id):
    message = u'Отлично! Расскажи мне какие работы ты хочешь сделать на нащем сервисе. Обязательно укажи марку/модель' \
              u' автомобиля, гос.номер и VIN'
    block_user(user_id, u'repair')
    return message, ''

info_command = command_system.Command()

info_command.keys = [u'ремонт', u'repair', u'записаться на ремонт']
info_command.description = u'Запишу на ремонт'
info_command.process = info
