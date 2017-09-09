#!/bin/python2
# coding=UTF-8

from bot_session import unblock_user

def unblock(user_id, body):
    if body == 'unblock':
        unblock_user(user_id)
        return u'Вы разблокированны', ''
    else:
        return u'unblock для разблокировки', ''
