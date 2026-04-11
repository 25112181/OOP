#Bai tap 5: Lop circle
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def point_in_circle(self, point):
        d = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
        return d <= self.radius

    def rect_in_circle(self, rect_points):
        for p in rect_points:
            if not self.point_in_circle(p):
                return False
        return True

    def rect_circle_overlap(self, rect_points):
        for p in rect_points:
            if self.point_in_circle(p):
                return True
        return False

center = Point(0, 0)
circle = Circle(center, 5)

p = Point(3, 4)
print("Point in circle:", circle.point_in_circle(p))
