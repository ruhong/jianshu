#-*- coding:utf-8 -*-

#这就是我，世界上独一无二
class Me(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(cls.__class__, cls).__new__(
                                 cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__name = "Mr.Zhou"
        self.__height = "120"
        self.__gender = "man"

    def getName(self):
        return self.__name

    def getHeight(self):
        return self.__height

    def getGender(self):
        return self.__gender

    def getIntroduction(self):
        return "Hi, I am " + self.__name + ", " + self.__height + ", and a " + self.__gender + "."

if __name__ == "__main__":
    m1 = Me()
    m2 = Me()

    print m1 == m2
    print m1.getIntroduction()

"""print out

True
Hi, I am Mr.Zhou, 120, and a man.
"""
