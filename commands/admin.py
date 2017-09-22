# coding=UTF-8
import command_system
from bot_session import check_admin, block_user


def admin(user_id):
    if check_admin(user_id):
        block_user(user_id, 'admin_start')
        message = u'Выберете действие:\n' \
                  u'1. Обновить список шин\n' \
                  u'2. Управление акциями\n' \
                  u'3. Управление администраторами\n' \
                  u'Введите номер требуемого действия, "выход" для отмены'
        return message, ''
    else:
        return u'К сожалению у вас нет прав администратора', ''


hello_command = command_system.Command()

hello_command.keys = [u'админ', u'админка', u'admin']
hello_command.description = u'Админ диалог'
hello_command.process = admin
hello_command.view = False
