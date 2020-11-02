class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.__length = length
        self.__width = width

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def setSide(self, s):
        Rectangle.setLength(self, s)
        Rectangle.setWidth(self, s)

    def getSide(self):
        return self.getWidth()

    def setLength(self, l):
        Rectangle.setLength(self, l)
        Rectangle.setWidth(self, l)

    def setWidth(self, l):
        Rectangle.setLength(self, l)
        Rectangle.setWidth(self, l)

sq = Square(3)
sq.setSide(5)
sq.setLength(4)
print(sq.getWidth())
print(sq.getLength())