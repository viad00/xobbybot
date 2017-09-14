# coding=UTF-8

from bot_session import unblock_user, get_sale_by_id

sorry = u'Извини, я не понимаю. Введи номер акции (например "1"). Если ты передумал(а) и хочешь задать ' \
                   u'другой вопрос, пиши "выход"'


def get_sale(user_id, answer):
    if answer == u'выход':
        unblock_user(user_id)
        return u'Спасибо за обращение! Чтобы узнать о командах введите "помощь"', ''
    else:
        try:
            sale_id = int(answer)
        except Exception:
            return sorry, ''
        sale = get_sale_by_id(sale_id)
        if sale == None:
            return sorry, ''
        else:
            unblock_user(user_id)
            return sale[0], sale[1]
