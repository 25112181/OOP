#Bai tap 3: Xay dung lop phan so
class MauSoBangKhong(Exception):
    pass
class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong("Mau so khong duoc bang 0")
        self.__tu = tu
        self.__mau = mau
        self.toi_gian()  
    @property
    def tu(self):
        return self.__tu
    @property
    def mau(self):
        return self.__mau

    def ucln(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def toi_gian(self):
        u = self.ucln(abs(self.__tu), abs(self.__mau))
        self.__tu //= u
        self.__mau //= u
        if self.__mau < 0:
            self.__tu *= -1
            self.__mau *= -1

    def is_toi_gian(self):
        return self.ucln(abs(self.__tu), abs(self.__mau)) == 1

    def __add__(self, other):
        tu = self.__tu * other.__mau + other.__tu * self.__mau
        mau = self.__mau * other.__mau
        return PhanSo(tu, mau)

    def __sub__(self, other):
        tu = self.__tu * other.__mau - other.__tu * self.__mau
        mau = self.__mau * other.__mau
        return PhanSo(tu, mau)

    def __mul__(self, other):
        return PhanSo(self.__tu * other.__tu, self.__mau * other.__mau)

    def __truediv__(self, other):
        return PhanSo(self.__tu * other.__mau, self.__mau * other.__tu)

    def __eq__(self, other):
        return self.__tu == other.__tu and self.__mau == other.__mau

    def __lt__(self, other):
        return self.__tu * other.__mau < other.__tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.__mau > other.__tu * self.__mau

    def __str__(self):
        if self.__mau == 1:
            return f"{self.__tu}"
        return f"{self.__tu}/{self.__mau}"
ds = []

n = int(input("Nhap so luong phan so: "))

for i in range(n):
    print(f"Phan so {i+1}:")
    tu = int(input("  Tu: "))
    mau = int(input("  Mau: "))
    try:
        ps = PhanSo(tu, mau)
        ds.append(ps)
    except MauSoBangKhong as e:
        print("Lỗi:", e)

print("\nDanh sach phan so (đa toi gian):")
for ps in ds:
    print(ps)
ds.sort()
print("\nSau khi sap xep tang dan:")
for ps in ds:
    print(ps)
