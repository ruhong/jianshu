#-*- coding:utf-8 -*-

from copy import deepcopy

#心形原型
class HeartShape(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def clone(self):
        return deepcopy(self)

#心形工厂
class HeartShapeFactory(object):
    def __init__(self, obj):
        self.obj = obj
    def getHeartShape(self):
        return self.obj.clone()

if __name__ == "__main__":
    heartShapeFactory = HeartShapeFactory(HeartShape("red", "big"))

    #红色大心形，要多少有多少
    a = heartShapeFactory.getHeartShape()
    b = heartShapeFactory.getHeartShape()

    print a.color
    print b.color

    print "------------------"
    
    a.color = "yellow"
    print a.color
    print b.color

"""print out

red
red
------------------
yellow
red
"""