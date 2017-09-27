# coding=UTF-8

import command_system
from bot_session import block_user, test_start, test_get_question


def tyres(user_id):
    message = u'Хорошо, давай начнём!\n'
    block_user(user_id, 'test')
    test_start(user_id)
    text, attach = test_get_question(0)
    return message + text + u'\nНапиши номер правильного ответа', attach


info_command = command_system.Command()

info_command.keys = [u'тест', u'начать тест', u'test']
info_command.description = u'Пройти тест.'
info_command.process = tyres
