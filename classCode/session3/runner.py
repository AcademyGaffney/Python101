from point import Point
from segment import Segment

p = Point(4, 5)
p2 = Point(3,7)

s = Segment(p, p2)
print(p == p2)
print(s)

p2.movePoint(1, -2)
print(p == p2)
print(s)

print(p.__doc__)

