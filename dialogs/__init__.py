import os, importlib

def load_modules():
   dirs = os.listdir("dialogs")
   for dir in dirs:
        modules = filter(lambda x: x.endswith('.py'), os.listdir("dialogs/" + dir))
        for m in modules:
            importlib.import_module("dialogs." + dir + m[0:-3])