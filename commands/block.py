# coding=UTF-8
import command_system
from bot_session import block_user


def block(user_id):
    block_user(user_id, 'unblock')
    message = u'Я заблокировал'
    return message, ''

block_command = command_system.Command()

block_command.keys = [u'blockme']
block_command.description = u'Заблокирую тебя'
block_command.process = block
block_command.view = False
