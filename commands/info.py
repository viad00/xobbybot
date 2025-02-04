# coding=UTF-8
import command_system


def info(user_id):
    message = u'Я знаю следующие команды:\n'
    for c in command_system.command_list:
        if c.view:
            message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''

info_command = command_system.Command()

info_command.keys = [u'помощь', u'помоги', u'help']
info_command.description = u'Покажу список команд'
info_command.process = info
