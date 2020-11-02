from point import Point

class Segment:

    def __init__(self, a, b):
        self.__a = Point(a.getX(), a.getY())
        self.__b = Point(b.getX(), b.getY())

    def getA(self):
        return Point(self.__a.getX(), self.__a.getY())

    def getB(self):
        return self.__b

    def setA(self, a):
        self__a = a

    def setB(self, b):
        self__b = b

    def __str__(self):
        return str(self.__a) + "--" +str(self.__b)
