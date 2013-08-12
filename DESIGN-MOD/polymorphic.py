#-*-coding:utf-8 -*-

#画家可以画画
class Painter(object):
    def working(self):
        return "painter is working."

#歌手可以唱歌
class Singer(object):
    def working(self):
        return "singer is working."

#音乐家可以弹奏
class Pianist(object):
    def working(self):
        return "pianist is working."

 #不管有多少角色，代码就这么多，是不是低耦合，很高效尼
class MovieAction(object):
    def getAction(self, obj):
            return obj.working()

if __name__ == "__main__":
    movieAction = MovieAction()
    print movieAction.getAction(Singer())
    print movieAction.getAction(Pianist())

"""print out

singer is working.
pianist is working.
"""