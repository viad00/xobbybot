# coding=UTF-8
import smtplib
from email.mime.text import MIMEText
import vkapi

EMAIL_DEST = 'viad.2000@yandex.ru'
EMAIL_FROM = 'viad.2000@yandex.ru'
EMAIL_SERVER = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_LOGIN = 'viad-2000'
EMAIL_PASS = 'cmmaycjlkhjihxgh'


def send_mail(text, user_id, reason):
    smtpObj = smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT)
    smtpObj.starttls()
    smtpObj.login(EMAIL_LOGIN, EMAIL_PASS)
    msg = MIMEText(text  + u'\n\nСсылка на страницу вк: https://vk.com/id' + str(user_id), 'plain', 'utf-8')
    msg['Subject'] = reason + u' от ' + vkapi.get_name(user_id)
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_DEST
    smtpObj.sendmail(EMAIL_FROM, EMAIL_DEST, msg.as_string())
    smtpObj.quit()
