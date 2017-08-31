#!/bin/python
# coding=UTF-8
from flask import Flask, json, request
import messageHandler
from settings import *
import commands.hello

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
        print(str(request.data))
        return 'ok'


@app.route('/')
def hello():
    return "HELLO"

app.run(host='0.0.0.0', debug=True)
