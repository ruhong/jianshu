#-*- coding:utf-8 -*-

#装饰者
class Decorator(object):
    def __init__(self, *args):
        if args:
            self.obj = args[0]
        else:
            self.obj = None

    def getPrice(self):
        if self.obj:
            return self.obj.getPrice() + ', ' + self.name + ': ' + str(self.price)
        else:
            return self.name + ': ' + str(self.price)

    def getCost(self):
        if self.obj:
            return float(self.obj.getCost()) + float(self.price)
        else:
            return float(self.price)
#新发型
class NewHair(Decorator):
    def __init__(self, *args):
        self.name = "new hair style"
        self.price = "20"
        super(self.__class__, self).__init__(*args)
#新衣服
class NewCloth(Decorator):
    def __init__(self, *args):
        self.name = "new cloth"
        self.price = "200"
        super(self.__class__, self).__init__(*args)
#新鞋子
class NewShoes(Decorator):
    def __init__(self, *args):
        self.name = "new shoes"
        self.price = "130"
        super(self.__class__, self).__init__(*args)

if __name__ == "__main__":
    #我的所有装备
    equipment = NewHair()
    equipment = NewCloth(equipment)
    equipment = NewShoes(equipment)

    print equipment.getPrice()
    print "total cost: ", equipment.getCost()

"""print out

new hair style: 20, new cloth: 200, new shoes: 130
total cost:  350.0
"""
