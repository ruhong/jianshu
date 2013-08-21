#-*- coding:utf-8 -*-

#支付系统
class PaySystm(object):
    def pay(self):
        print "Payments completed."
#卖家系统
class SellerSystem(object):
    def sendOut(self):
        print "Seller sended out."
#快递系统
class ExpressSystem(object):
    def express(self):
        print "Expressors delivered."

#高层接口，简单易用，只能支付一次哦
class Facade(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            paySys = PaySystm()
            paySys.pay()

            sellerSys = SellerSystem()
            sellerSys.sendOut()

            expSys = ExpressSystem()
            expSys.express()

            cls.__instance = super(cls.__class__, cls).__new__(
                                 cls, *args, **kwargs)
        return cls.__instance

if __name__ == "__main__":
    facade = Facade()

"""

Payments completed.
Seller sended out.
Expressors delivered.
"""
