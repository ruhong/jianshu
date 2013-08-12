#-*-coding:utf-8 -*-

class Flower(object):
    @classmethod
    def __str__(cls):
        return cls.enName + ": " + cls.zhName

class Petunia(Flower):
    enName = "petunia"
    zhName = "牵牛花"

class Heronsbill(Flower):
    enName = "Heronsbill"
    zhName = "太阳花"

    def __str__(self):
        return super(self.__class__, self).__str__() + ", I like it very much."

if __name__ == "__main__":
    petunia  = Petunia()
    heronsbill = Heronsbill()
    print petunia
    print heronsbill