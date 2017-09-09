#!/bin/python2
# coding=UTF-8
from bot_session import getRoute
from routes import *

def route(user_id, body):
    rout = getRoute(user_id)
    return routes[rout](user_id, body)
