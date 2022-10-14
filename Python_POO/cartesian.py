import math

class Point:
    __cXPos =0 
    __cYPos = 0

    def __init__(self, x=0.0, y=0.0):
        self.__cXPos = x
        self.__cYPos = y

    def getx(self):
        return self.__cXPos

    def gety(self):
        return self.__cYPos

    def distance_from_xy(self, x, y):
        return (math.hypot(self.__cXPos - x, self.__cYPos-y))

    def distance_from_point(self, point):
        return (math.hypot(self.__cXPos - point.getx(), self.__cYPos-point.gety()))

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
