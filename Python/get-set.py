#-*- coding:utf-8 -*-

"""
@propery 设置属性只读，当试图改变属性值是将报错
@name.setter 设置属性可写
@name.deleter 设置属性可删除

个人觉得这样写很蛋疼，直接定义
class Flower(object):
    def __init__(self):
        self.name = "XXX"

这样不就得了，让那么大弯子干嘛，
如果定义私有的属性，前面加双下划线即可。
"""

class Flower(object):
    def __init__(self):
        self._name = "太阳花"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

if __name__ == "__main__":
    flower = Flower()
    print flower.name

    flower.name = "牵牛花"
    print flower.name

    del flower.name
    print flower.name
