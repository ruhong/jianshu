#-*-coding:utf-8 -*-

#KFC store
class KFCStore():
    def getChikenWing(self):
        return "DFC chicken wing."

#MCD store
class MCDStore():
    def getChikenWing(self):
        return "MCD chicken wing."

#ChickenWing Factory
class ChickenWingFactory(object):
    def createChickenWing(self, obj):
        return obj.getChikenWing()

if __name__ == "__main__":
    chickenWingFactory = ChickenWingFactory()
    print chickenWingFactory.createChickenWing(KFCStore())
    print chickenWingFactory.createChickenWing(MCDStore())

"""print out

DFC chicken wing.
MCD chicken wing.
"""
