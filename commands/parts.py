# coding=UTF-8
import command_system
from bot_session import block_user


def parts(user_id):
    message = u'Отлично! Расскажи мне какие запчасти ты хочешь приобрести. Обязательно укажи марку/модель автомобиля,' \
              u' гос.номер и VIN. '
    block_user(user_id, u'parts')
    return message, ''


info_command = command_system.Command()

info_command.keys = [u'запчасти', u'parts', u'купить запчасти', u'заказ запчастей']
info_command.description = u'Закажу запчасти'
info_command.process = parts
