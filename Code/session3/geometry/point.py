import math

class Point:

    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def setPoint(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def movePoint(self, x, y):
        self.__x += x
        self.__y += y

    def moveX(self, x):
        self.__x += x

    def moveY(self, y):
        self.__y += y

    def getDegrees(self):
        degrees = math.atan2(self.__x, self.__y) / math.pi * 180
        if degrees < 0:
            return degrees + 360
        return degrees

    def getDistance(self):
        return (self.__x ** 2 + self.__y ** 2) ** .5

    def __str__(self):
        return "({},{})".format(self.__x, self.__y)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        xQuot = self.__x / other.__x
        yQuot = self.__y / other.__y
        if xQuot < 1:
            xQuot = 1 / xQuotS
        if yQuot < 1:
            yQuot = 1 / yQuot
        return xQuot < 1.000000000001 and yQuot < 1.000000000001

