# coding=UTF-8

from bot_session import tools_write_db, unblock_user
import mail_sender


def tools_write(user_id, answer):
    unblock_user(user_id)
    tools_write_db(user_id, answer)
    mail_sender.send_mail(answer, user_id, u'Заказ товаров')
    return u'Отлично! Через некторое время с тобой свяжется менеджер. Кстати,' \
           u' у нас действуют акции. Хочешь узнать как получить бонус? Пиши "акции".', ''
