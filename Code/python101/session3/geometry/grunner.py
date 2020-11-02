from point import Point
from segment import Segment

p = Point(5, 7.14)
q = Point(8, 3.14)


s = Segment(p, q)
print(s)

q.movePoint(-3, 4)
print(s)
print(p == q)


