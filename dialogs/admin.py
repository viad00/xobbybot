# coding=UTF-8
# ex: [{u'doc': {u'access_key': u'5db837c7db3d78e92a', u'title': u'\u0410\u043d\u0430\u043b\u0438\u0437\u044b.pdf',
#  u'url': u'https://vk.com/doc143264621_450818813?hash=1d5282494326188340&dl=GE2DGMRWGQ3DEMI:1506120603:8e1b2af3256a4d2ae3&api=1&no_preview=1',
# u'ext': u'pdf', u'date': 1506120593, u'owner_id': 143264621, u'type': 1, u'id': 450818813, u'size': 431407}, u'type': u'doc'}]
from bot_session import block_user, unblock_user, tyres_get_fix_price, tyres_get_install_price, tyres_get_store_price, \
    admins_get_all, get_all_sales, tyres_set_service_price, admin_del_by_id, add_admin, sale_del_by_id, sale_add, sale_add_p1
import urlparse, urllib, hashlib, os
import vkapi
import tyres_import

return_f = u'Возврат \n' + u'Выберете действие:\n' \
                  u'1. Обновить список шин\n' \
                  u'2. Управление акциями\n' \
                  u'3. Управление администраторами\n' \
                  u'4. Обновить цены на стоимость работ для шин\n' \
                  u'Введите номер требуемого действия, "выход" для отмены'
tyres_gag = u'Выберите цену для обновления:\n' \
               u'1. Стоимость работ по шиномонтажу: {0}\n' \
               u'2. Стоимость хранения шин: {1}\n' \
               u'3. Стоимость работ по регулировке сход-развал: {2}\n' \
               u'Укажите номер цены для редактирования или "выход"'


def start(user_id, answer, attach):
    if answer == u'1':
        unblock_user(user_id)
        block_user(user_id, 'admin_stock')
        return u'Отправте в ответ на это сообщение xls таблицу в приложении', ''
    elif answer == u'2':
        unblock_user(user_id)
        block_user(user_id, 'admin_sales')
        message = u'Текущий список акций:\n'
        for row in get_all_sales():
            message += str(row[0]) + u': ' + row[1] + u'\n'
        message += u'Укажите номер акции для удаления или "добавить" для добавления акции или "выход"'
        return message, ''
    elif answer == u'3':
        unblock_user(user_id)
        block_user(user_id, 'admin_admin')
        message = u'Текущий список администраторов:\n'
        for row in admins_get_all():
            message += str(row[0]) + u': ' + row[1] + ' - ' + vkapi.get_name(row[1]) + u'\n'
        message += u'Укажите номер администратора для удаления или "добавить" для добавления администратора или "выход"'
        return message, ''
    elif answer == u'4':
        unblock_user(user_id)
        block_user(user_id, 'admin_price')
        return tyres_gag.format(tyres_get_install_price(), tyres_get_store_price(), tyres_get_fix_price()), ''
    elif answer == u'выход':
        unblock_user(user_id)
        return u'Вы вышли из системы', ''
    else:
        return u'Прости, я тебя не понимаю. главное меню @Админка', ''


def stock(user_id, answer, attach):
    try:
        if attach[0]['doc']['ext'] == 'xls':
            path = 'images/new_tyres.xls'
            try:
                os.remove(path)
            except Exception:
                pass
            urllib.urlretrieve(attach[0]['doc']['url'], path)
            tyres_import.process_import(path)
            os.remove(path)
            unblock_user(user_id)
            block_user(user_id, 'admin_start')
            return u'Успешно импотированн ассортимент шин', ''
        elif answer == u'выход' or answer == u'отмена' or answer == u'exit':
            unblock_user(user_id)
            block_user(user_id, 'admin_start')
        else:
            return u'Неверный формат файла xls != {0}'.format(attach[0]['doc']['ext']), ''
    except Exception as e:
        return u'Ошибка\n' + str(e) + '\n' + str(e.args), ''


def sales(user_id, answer, attach):
    unblock_user(user_id)
    try:
        row_id = int(answer)
        sale_del_by_id(row_id)
        block_user(user_id, 'admin_start')
        return u'Акция с id: {0} удалёна'.format(row_id), ''
    except Exception:
        if answer == u'добавить':
            block_user(user_id, 'admin_sale_add')
            return u'Укажите название (краткое описание) акции', ''
        elif answer == u'выход':
            block_user(user_id, 'admin_start')
            return return_f, ''
        else:
            block_user(user_id, 'admin_sales')
            return u'Я не понимаю. акции @Админка', ''


def add_sale(user_id, answer, attach):
    unblock_user(user_id)
    ret = u'Произошла ошибка проверьте данные\n'
    try:
        sale_add(answer)
        ret = u'Укажите описание, при необходимости прикрепите картинки\n'
    except Exception:
        pass
    block_user(user_id, 'admin_sale_add_p1')
    return ret, ''


def add_sale_p1(user_id, answer, attach):
    unblock_user(user_id)
    ret = u'Произошла ошибка проверьте данные\n'
    try:
        attack = u''
        down = []
        if len(attach) > 0:
            for row in attach:
                try: # Зато работает)
                    down.append(row['photo']['photo_2560'])
                except Exception:
                    try:
                        down.append(row['photo']['photo_1280'])
                    except Exception:
                        try:
                            down.append(row['photo']['photo_807'])
                        except Exception:
                            try:
                                down.append(row['photo']['photo_604'])
                            except Exception:
                                try:
                                    down.append(row['photo']['photo_130'])
                                except Exception:
                                    try:
                                        down.append(row['photo']['photo_75'])
                                    except Exception:
                                        pass
            for url in down:
                name = hashlib.md5(url).hexdigest()
                urllib.urlretrieve(url, 'images/' + name + '.jpg')
                attack += name + ','
        sale_add_p1(answer, attack[:-1])
        ret = u'Успешно добавлена новая акция\n'
    except Exception:
        pass
    block_user(user_id, 'admin_start')
    return ret + return_f, ''


def admin(user_id, answer, attach):
    unblock_user(user_id)
    try:
        row_id = int(answer)
        admin_del_by_id(row_id)
        block_user(user_id, 'admin_start')
        return u'Пользователь с id: {0} удалён'.format(row_id), ''
    except Exception:
        if answer == u'добавить':
            block_user(user_id, 'admin_admin_add')
            return u'Укажите ссылку на станицу администратора', ''
        elif answer == u'выход':
            block_user(user_id, 'admin_start')
            return return_f, ''
        else:
            return u'Я не понимаю. администраторы @Админка', ''


def admin_add(user_id, answer, attach):
    unblock_user(user_id)
    ret = u'Произошла ошибка проверьте данные\n'
    try:
        o = urlparse.urlparse(answer)
        add_admin(str(vkapi.get_user_id(o.path[1:])))
        ret = u'Успешно добавлен администратор\n'
    except Exception:
        pass
    block_user(user_id, 'admin_start')
    return ret + return_f, ''


def price(user_id, answer, attach):
    if answer == u'1':
        new_route = 'admin_price_install'
    elif answer == u'2':
        new_route = 'admin_price_store'
    elif answer == u'3':
        new_route = 'admin_price_fix'
    elif answer == u'выход':
        unblock_user(user_id)
        block_user(user_id, 'admin_start')
        return return_f, ''
    else:
        return u'Прости, не понимаю. управление ценами @Админка', ''
    unblock_user(user_id)
    block_user(user_id, new_route)
    return u'Укажите новую цену. Примечание: может быть любой строкой', ''


def price_install(user_id, answer, attach):
    unblock_user(user_id)
    block_user(user_id, 'admin_price')
    tyres_set_service_price(u'install', answer)
    return u'Цена обновленна\n' + tyres_gag.format(tyres_get_install_price(), tyres_get_store_price(), tyres_get_fix_price()), ''


def price_store(user_id, answer, attach):
    unblock_user(user_id)
    block_user(user_id, 'admin_price')
    tyres_set_service_price(u'store', answer)
    return u'Цена обновленна\n' + tyres_gag.format(tyres_get_install_price(), tyres_get_store_price(), tyres_get_fix_price()), ''


def price_fix(user_id, answer, attach):
    unblock_user(user_id)
    block_user(user_id, 'admin_price')
    tyres_set_service_price(u'fix', answer)
    return u'Цена обновленна\n' + tyres_gag.format(tyres_get_install_price(), tyres_get_store_price(), tyres_get_fix_price()), ''
