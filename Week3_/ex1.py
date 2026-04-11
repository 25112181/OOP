#Bai tap 1 - Lop point - 2D Geometry
import math 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def display(self):
        print(f"({self.x}, {self.y})")

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2) 

    def symmetry(self):
        return Point(-self.x, -self.y)

print("Bai tap 1 - Lop point - 2D Geometry")   

# A(3, 4)
A = Point (3, 4)
print("A: ", end=" ")
A.display()

# B nhap tu ban phim
x = float(input("Nhap x cua B: "))
y = float(input("Nhap y cua B: "))
B = Point(x, y)
print("B: ", end=" ")
B.display()

#C doi xung qua O
C = B.symmetry()
print("Doi xung B qua O: ", end=" ")
C.display()

#Khoang cach B toi O va A toi B
print("Khoang cach B toi O: ", B.distance_to_origin())
print("Khoang cach A toi B: ", A.distance_to(B))
