# coding=UTF-8

from bot_session import tyres_write_size, block_user, unblock_user
import re


def write_query(user_id, answer):
    if re.findall(r'\d+/\d+/\d+', answer):
        unblock_user(user_id)
        tyres_write_size(user_id, re.findall(r'\d+/\d+/\d+', answer)[0])
        # TODO: Next step
        return u'Напиши тип шин: "лето" или "зима"', ''
    elif answer == u'отмена':
        unblock_user(user_id)
        return u'Хорошо! Если тебе нужна помощь, пиши "помощь"', ''
    else:
        return u'Извини, я не понимаю. Введи размер шины в формате 195/65/15. ' \
               u'Если ты передумал(а) и хочешь задать другой вопрос, пиши "отмена"', ''
