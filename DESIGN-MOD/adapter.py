#-*- coding:utf-8 -*-

#充电器--Iphone专用
class Charger(object):
    def charge(self):
        print "A charger for Iphone."

#万能充
class ChargerAdapter(Charger):
    def charge(self):
        print "A charger for phones."

if __name__ == "__main__":
    iphoneCharger = Charger()
    iphoneCharger.charge()

    phoneCharger = ChargerAdapter()
    phoneCharger.charge()

"""print out

A charger for Iphone.
A charger for phones.
"""