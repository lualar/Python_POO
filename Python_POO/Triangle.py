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

class Triangle:
    __Point1 = Point()
    __Point2 = Point()
    __Point3 = Point()

    __Dist1 = 0
    __Dist2 = 0
    __Dist3 = 0

    def __init__(self, vertice1, vertice2, vertice3):
        self.__Point1 = vertice1
        self.__Point2 = vertice2
        self.__Point3 = vertice3

    def perimeter(self):
        self.__Dist1 = self.__Point1.distance_from_point(self.__Point2)
        self.__Dist2 = self.__Point2.distance_from_point(self.__Point3)
        self.__Dist3 = self.__Point3.distance_from_point(self.__Point1)
        return self.__Dist1 + self.__Dist2 + self.__Dist3
       
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

