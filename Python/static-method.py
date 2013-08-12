#-*-coding:utf-8 -*-

class Heronsbill(object):
    enName = "heronsbill"
    zhName = "太阳花"

    @staticmethod
    def flowerName():
        return Heronsbill.zhName

if __name__ == "__main__":
    print Heronsbill.flowerName()