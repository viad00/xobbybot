# coding=UTF-8
from bot_session import getRoute
from routes import *


def route(user_id, body, attach):
    rout = getRoute(user_id)
    if rout[0:5] == 'admin':
        return routes[rout](user_id, body, attach)
    else:
        return routes[rout](user_id, body)
