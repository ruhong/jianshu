#-*- coding: utf-8 -*-

#汉堡抽象工厂
class HamburgerFactory(object):
    def createHamburger(self):
        pass

#汉堡里加辣椒的工厂
class HamburgerWithPepperFacotry(HamburgerFactory):
    def createHamburger(self):
        print "A hamburder with pepper is ready."

#汉堡里加火腿的工厂
class HamburgerWithHamFacotry(HamburgerFactory):
    def createHamburger(self):
        print "A hamburder with ham is ready."

#美眉A 喜欢吃辣椒
class MeiMeiA(object):
    def getHamburder(self):
        print "I want to a hanburger with pepper."
        hamburgerFactory = HamburgerWithPepperFacotry()
        hamburgerFactory.createHamburger()

#美眉B 喜欢吃火腿
class MeiMeiB(object):
    def getHamburder(self):
        print "I want to a hanburger with ham."
        hamburgerFactory = HamburgerWithHamFacotry()
        hamburgerFactory.createHamburger()

if __name__ == "__main__":
    mA = MeiMeiA()
    mA.getHamburder()

"""print out

I want to a hanburger with pepper.
A hamburder with pepper is ready.
"""