#-*- coding:utf-8 -*-

#套餐A
class MealA(object):
    def mainFood(self):
        print "main food is ready."
    def sideFood(self):
        print "side food is ready."
    def drink(self):
        print "drink is ready."

#套餐B
class MealB(object):
    def mainFood(self):
        print "main food is ready."
    def sideFood(self):
        print "side food is ready."
    def drink(self):
        print "drink is ready."

#服务生
class Waiter(object):
    def deliver(self, meal):
        meal.mainFood()
        meal.sideFood()
        meal.drink()

if __name__ == "__main__":
    waiter = Waiter()
    waiter.deliver(MealA())

"""print out

main food is ready.
side food is ready.
drink is ready.
"""