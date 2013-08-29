#-*- coding:utf-8 -*-

#TV
class TV(object):
    def __init__(self, brand, size):
        self.brand = brand
        self.size = str(size)

#TV工厂
class TVFactory(object):
    createdTV = {}

    @staticmethod
    def createTV(brand, size):
        tvStyle = brand+str(size)
        if TVFactory.createdTV.has_key(tvStyle):
            return TVFactory.createdTV[tvStyle]
        else:
            tv = TV(brand, size)
            TVFactory.createdTV[tvStyle] = tv
            return tv

#TV管理器
class TVManager(object):
    tvDatabase = {}

    def addNewTV(self, owner, brand, size):
        tv = TVFactory.createTV(brand, size)
        self.__class__.tvDatabase[owner] = tv

    def showTV(self):
        for item in self.__class__.tvDatabase:
            print item + ": " + self.__class__.tvDatabase[item].brand + ", " + self.__class__.tvDatabase[item].size

if __name__ == "__main__":

    tvManager = TVManager()
    #同一品牌、同一尺寸的TV只会共享一个实例
    tvManager.addNewTV("adult", "TCL", 30)
    tvManager.addNewTV("children", "TCL", 30)
    tvManager.showTV()

"""print out

adult: TCL, 30
children: TCL, 30
"""