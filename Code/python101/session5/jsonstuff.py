import json
from point import Point
from segment import Segment


s = Segment(Point(3,5), Point(7, 1))

j = json.dumps(s)

print(j)

