#!/bin/python2
# coding=UTF-8
import vkapi
import os
import importlib
from command_system import command_list
from bot_session import check_session
from routerHandler import route


def load_modules():
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])


def get_answer(body, user_id, attach, original):
   if check_session(user_id):
       message, attachment = route(user_id, body, attach, original)
       return message, attachment
   message = u"Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
   attachment = ''
   distance = len(body)
   command = None
   key = ''
   for c in command_list:
       for k in c.keys:
           d = damerau_levenshtein_distance(body, k)
           if d < distance:
               distance = d
               command = c
               key = k
               if distance == 0:
                   message, attachment = c.process(user_id)
                   return message, attachment
   if distance < len(body)*0.4:
       message, attachment = command.process(user_id)
       message = u'Я понял ваш запрос как "%s"\n\n' % key + message
   return message, attachment


def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   try:
      attachments = data['attachments']
   except Exception:
      attachments = []
   message, attachment = get_answer(data['body'].lower(), user_id, attachments, data['body'])
   vkapi.send_message(user_id, token, message, attachment)


def damerau_levenshtein_distance(s1, s2):
   d = {}
   lenstr1 = len(s1)
   lenstr2 = len(s2)
   for i in range(-1, lenstr1 + 1):
       d[(i, -1)] = i + 1
   for j in range(-1, lenstr2 + 1):
       d[(-1, j)] = j + 1
   for i in range(lenstr1):
       for j in range(lenstr2):
           if s1[i] == s2[j]:
               cost = 0
           else:
               cost = 1
           d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
           )
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
   return d[lenstr1 - 1, lenstr2 - 1]
