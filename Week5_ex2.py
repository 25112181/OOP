#Bai tap 2: He thong quan li nhan vien phong ban
class Nhanvien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def tinhluong(self):
        return self.luong

    def inthongtin(self):
        print("Ten: ", self.ten)
        print("Luong: ", self.tinhluong())

class Congtacvien(Nhanvien):
    def __init__(self, ten, luong, thoihan, phucap):
        super().__init__(ten, luong)
        self.thoihan = thoihan
        self.phucap = phucap

    def tinhluong(self):
        return self.luong + self.phucap

    def inthongtin(self):
        super().inthongtin()
        print("Thoi han hop dong: ", self.thoihan)
        print("Phu cap: ", self.phucap)

class Nhanvienchinhthuc(Nhanvien):
    def __init__(self, ten, luong, vitri, ngayvaolam):
        super().__init__(ten, luong)
        self.vitri = vitri
        self.ngayvaolam = ngayvaolam

    def inthongtin(self):
        super().inthongtin()
        print("Vi tri: ", self.vitri)
        print("Ngay vao lam: ", self.ngayvaolam)


class Truongphong(Nhanvien):
    def __init__(self, ten, luong, ngayquanli, phucapquanli):
        super().__init__(ten, luong)
        self.ngayquanli = ngayquanli
        self.phucapquanli = phucapquanli

    def tinhluong(self):
        return self.luong + self.phucapquanli

    def inthongtin(self):
        super().inthongtin()
        print("Ngay quan li: ", self.ngayquanli)
        print("Phu cap quan li: ", self.phucapquanli)

print("=== Cong tac vien ===")
ctv = Congtacvien("Mp", 5000000, "6 thang", 2000000)
ctv.inthongtin()

print("\n=== Nhan vien chinh thuc ===")
nvct = Nhanvienchinhthuc("Mp2", 100000000, "Nhan vien van phong", "2022-12-04")
nvct.inthongtin()

print("\n=== Truong phong ===")
tp = Truongphong("Mp3", 20000000, "2022-04-24", 5000000)
tp.inthongtin()
