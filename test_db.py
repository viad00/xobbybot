# coding=UTF-8

from bot_session import check_session, block_user, unblock_user, getRoute


def check():
    user_id = u'123456'
    try:
        check_session(user_id)
        block_user(user_id, 'test')
        if getRoute(user_id) == 'test':
            unblock_user(user_id)
            return True
        else:
            return False
    except Exception as e:
        print(u'ERROR: {0}'.format(e))
        return False


if __name__ == '__main__':
    print(check())
