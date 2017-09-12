#!/bin/python2
# coding=UTF-8
from flask import Flask, json, request
import messageHandler
from settings import *
import vkapi

app = Flask(__name__)


# Сюда приходит callback
@app.route('/test_bot', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return VK_CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], VK_TOKEN)
        return 'ok'
    elif data['type'] == 'message_allow':
        message = u'Привет!\nЯ чат-бот автосервиса Хобби-Авто.\nНаш сайт http://www.hobbyauto.ru\nБуду рад ответить на ' \
                  u'возникшие вопросы!\nНапиши "помощь" для списка комманд.'
        vkapi.send_message(data['object']['user_id'], VK_TOKEN, message, '')
        return 'ok'


@app.route('/')
def hello():
    return "HELLO"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
