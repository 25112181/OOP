#Bai tap 2: Lop Linesegment
import math

class Point:
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y

    def copy(self):
          return Point(self.x, self.y)

class LineSegement:
    def __init__(self, p1=None, p2=None):
        if p1 is None:
           p1 = Point()
        if p2 is None:
           p2 = Point()

        self.__d1 = p1.copy()
        self.__d2 = p2.copy()
  
    def get_d1(self):
        return self.__d1
    def get_d2(self):
        return self.__d2
    
    def set_d1(self, p):
        self.__d1 = p.copy()
    def set_d2(self, p):
        self.__d2 = p.copy()

    def length(self):
        return math.sqrt((self.__d1.x - self.__d2.x)**2 + (self.__d1.y - self.__d2.y)**2)

    def display(self):
        print(f"({self.__d1.x}, {self.__d1.y}) -> ({self.__d2.x}, {self.__d2.y})")

p1 = Point(1, 2)
p2 = Point(3, 6)

line = LineSegement(p1, p2)
line.display()
print("Length: ", line.length())
