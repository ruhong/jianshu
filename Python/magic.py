#-*- coding:utf-8 -*-

class A(object):
    def __init__(self):
        self.name = "A"
        print "__init__ is called."

    def __new__(cls, *args, **kwargs):
        print "__new__ is called."
        return super(cls.__class__, cls).__new__(cls, *args, **kwargs)
    def getName(self):
        return self.name

    def __call__(self):
        print "__call__ is called."


if __name__ == "__main__":
    a = A()
    print a.getName()
    a()
