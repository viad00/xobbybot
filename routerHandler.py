# coding=UTF-8
from bot_session import getRoute
from routes import *


def route(user_id, body, attach, original):
    rout = getRoute(user_id)
    if rout[0:5] == 'admin':
        if rout[6:10] == 'sale' or rout[6:10] == 'pric':
            return routes[rout](user_id, original, attach)
        else:
            return routes[rout](user_id, body, attach)
    else:
        return routes[rout](user_id, body)
