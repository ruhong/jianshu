#-*- coding:utf-8 -*-

#画家可以画画
class Painter(object):
    def paint(self):
        return "painter is working."

#歌手可以唱歌
class Singer(object):
    def sing(self):
        return "singer is working."

#音乐家可以弹奏
class Pianist(object):
    def play(self):
        return "pianist is working."

#当所需要的角色越来越多时，if else就越来越多，代码看起来将十分冗余，低效
class MovieAction(object):
    def getAction(self, role):
        if role == "painter":
            painter = paint()
            return painter.working()
        elif role == "singer":
            singer = Singer()
            return singer.sing()
        elif role == "pianist":
            pianist = Pianist()
            return pianist.play()
        else:
            return "Sorry, the role doesn't exist."


if __name__ == "__main__":
    movieAction = MovieAction()
    print movieAction.getAction('singer')
    print movieAction.getAction('shower')

"""print out

singer is working.
Sorry, the role doesn't exist.
"""