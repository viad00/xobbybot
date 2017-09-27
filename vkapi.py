import vk
import requests
from settings import *

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)


def get_user_id(screen_name):
    rs = api.users.get(user_ids=screen_name, fields='has_photo')
    return rs[0][u'id']


def get_name(user_id):
    rs = api.users.get(user_ids=user_id)
    return rs[0]['first_name'] + ' ' + rs[0]['last_name']


def upload_photo(user_id, binary):
    a = api.photos.getMessagesUploadServer(access_token=VK_TOKEN, peer_id=user_id)
    b = requests.post(a['upload_url'], files={'photo': binary}).json()
    c = api.photos.saveMessagesPhoto(access_token=VK_TOKEN, photo=b['photo'], server=b['server'], hash=b['hash'])
    d = 'photo{0}_{1}'.format(c[0]['owner_id'], c[0]['id'])
    return d
