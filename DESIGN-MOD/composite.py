#-*- coding:utf-8 -*-

#物品
class Stuff(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def des(self):
        print self.name + " : " + str(self.price)

#购物单
class Order(object):
    def __init__(self):
        self.orderComponentList = []
    #add方法可以添加物品、购物单哦
    def add(self, obj):
        self.orderComponentList.append(obj)
    def des(self):
        for stuff in self.orderComponentList:
            stuff.des()

if __name__ == "__main__":

    #美眉的购物单
    girlOrder = Order()
    girlOrder.add(Stuff("shoe", 120))
    girlOrder.add(Stuff("handbag", 220))
    girlOrder.add(Stuff("dress", 320))

    #我的的购物单
    boyOrder = Order()
    boyOrder.add(Stuff("T shirt", 230))

    #我俩的购物单，总之都是我付钱
    bothOrder = Order()
    bothOrder.add(girlOrder)
    bothOrder.add(boyOrder)
    bothOrder.des()

"""print out

shoe : 120
handbag : 220
dress : 320
T shirt : 230
"""
