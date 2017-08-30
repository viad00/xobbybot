import command_system


def hello():
   message = 'Привет, друг!\nЯ чат-бот автосервиса Хобби-Авто.\nДля списка комманд напиши "помощь"'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello
