# coding=UTF-8

from bot_session import tools_write_db, unblock_user


def tools_write(user_id, answer):
    unblock_user(user_id)
    tools_write_db(user_id, answer)
    return u'Отлично! Через некторое время с тобой свяжется менеджер. Кстати,' \
           u' у нас действуют акции. Хочешь узнать как получить бонус? Пиши "акции".', ''
