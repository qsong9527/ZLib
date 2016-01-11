# -*- coding: UTF-8 -*- 

#单例装饰器类
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class SingletonObject():

    def __init__(self):
        self.value = "201511301504"

    def say(self):
        print self.value
