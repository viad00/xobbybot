# coding=UTF-8
command_list = []


class Command:
   def __init__(self):
       self.__keys = []
       self.description = ''
       self.view = True
       command_list.append(self)

   @property
   def keys(self):
       return self.__keys

   @keys.setter
   def keys(self, mas):
       for k in mas:
           self.__keys.append(k.lower())

   def process(self, user_id):
       pass
