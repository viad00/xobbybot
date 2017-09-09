# coding=UTF-8
import command_system


def hello(user_id):
   message = u'Привет! Я бот Автоцентра ХОББИ-АВТО.\n Напиши "помощь" для списка команд.'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = [u'привет', u'hello', u'дратути', u'здравствуй', u'здравствуйте']
hello_command.description = u'Поприветствую тебя'
hello_command.process = hello
