#!/bin/python
# coding=UTF-8
from flask import Flask, json, request
import messageHandler
from settings import *

app = Flask(__name__)


# Сюда приходит callback
@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return VK_CONFIRMATION_TOKEN
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], VK_TOKEN)
        return 'ok'

app.run(debug = True)
