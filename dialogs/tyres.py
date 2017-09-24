# coding=UTF-8

from bot_session import tyres_write_size, block_user, unblock_user, tyres_find, tyres_get_size,\
    tyres_get_install_price, tyres_get_store_price, tyres_get_fix_price, tyres_write_order
import re
import mail_sender

exit_message = u'\nЕсли у тебя остались вопросы, пиши "заказ", "шиномонтаж", "хранение" или "сход-развал". ' \
                   u'Если у тебя больше нет вопросов, пиши "выход"'


def write_query(user_id, answer):
    if re.findall(r'\d+/\d+/\d+', answer):
        unblock_user(user_id)
        tyres_write_size(user_id, re.findall(r'\d+/\d+/\d+', answer)[0])
        block_user(user_id, 'tyres_season')
        return u'Напиши тип шин: "лето" или "зима"', ''
    elif answer == u'отмена':
        unblock_user(user_id)
        return u'Хорошо! Если тебе нужна помощь, пиши "помощь"', ''
    else:
        return u'Извини, я не понимаю. Введи размер шины в формате 195/65/15. ' \
               u'Если ты передумал(а) и хочешь задать другой вопрос, пиши "отмена"', ''


def find_tyres(user_id, answer):
    if answer == u'лето' or answer == u'зима':
        unblock_user(user_id)
        size = tyres_get_size(user_id)
        lst = tyres_find(size, answer)
        if len(lst) > 0:
            message = u'Шины по вашему запросу:\n'
            message += u'Название   Сезон   Цена\n'
            for row in lst:
                message += row[0] + '   ' + row[1] + '  ' + row[2] + u'р.\n'
        else:
            message = u'К сожалению по вашему запросу не нашлось шин.\n'
        message += u'Сделать заказ на шины  - пиши "заказ", узнать стоимость работ по шиномонтажу "шиномонтаж",' \
                   u' сезонное хранение "хранение", регулировка сход-развал - "сход-развал".\nЕсли помощь больше не ' \
                   u'требуется - "выход"'
        block_user(user_id, 'tyres_dialog')
        return message, ''
    elif answer == u'отмена':
        unblock_user(user_id)
        return u'Хорошо! Если тебе нужна помощь, пиши "помощь"', ''
    else:
        return u'Извини, я не понимаю. Напиши тип шин: "лето" или "зима". ' \
               u'Если ты передумал(а) и хочешь задать другой вопрос, пиши "отмена"', ''


def dialog_final(user_id, answer):
    if answer == u'заказ':
        unblock_user(user_id)
        block_user(user_id, 'tyres_order')
        return u'Отлично! Расскажи какие шины ты хочешь приобрести. Не забудь указать если тебе требуется подбор' \
               u' дисков, установка шин, их хранение или регулировка сход-развал.', ''
    elif answer == u'шиномонтаж':
        message = u'Стоимость работ по шиномонтажу:\n'
        return message + tyres_get_install_price() + exit_message, ''
    elif answer == u'хранение':
        message = u'Стоимость хранения шин:\n'
        return message + tyres_get_store_price() + exit_message, ''
    elif answer == u'сход-развал':
        message = u'Стоимость работ по регулировке сход-развал:\n'
        return message + tyres_get_fix_price() + exit_message, ''
    elif answer == u'выход':
        unblock_user(user_id)
        return u'Хорошо! Если тебе нужна помощь, пиши "помощь". Кстати, у нас действуют акции. ' \
               u'Хочешь узнать как получить бонус? Пиши "акции".', ''
    else:
        return u'Прости я тебя не понимаю.\n' + \
               u'Сделать заказ на шины  - пиши "заказ", узнать стоимость работ по шиномонтажу "шиномонтаж",' \
               u' сезонное хранение "хранение", регулировка сход-развал - "сход-развал".\nЕсли помощь больше не ' \
               u'требуется - "выход"', ''


def order(user_id, answer):
    unblock_user(user_id)
    tyres_write_order(user_id, answer)
    mail_sender.send_mail(answer, user_id, u'Заказ на шины')
    block_user(user_id, 'tyres_dialog')
    return u'Отлично! Через некторое время с тобой свяжется менеджер.' + exit_message, ''
