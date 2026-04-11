#Bai tap 3: Quan li can bo don vi san xuat
class CanBo:
    def __init__(self, ten, tuoi, gioiTinh, diaChi):
        self.ten = ten
        self.tuoi = tuoi
        self.gioiTinh = gioiTinh
        self.diaChi = diaChi

    def inTTin(self):
        print(f"Tên: {self.ten}, Tuổi: {self.tuoi}, Giới tính: {self.gioiTinh}, Địa chỉ: {self.diaChi}")

class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioiTinh, diaChi, bac):
        super().__init__(ten, tuoi, gioiTinh, diaChi)
        self.bac = bac 

    def inTTin(self):
        super().inTTin()
        print("Bậc:", self.bac)


class KySu(CanBo):
    def __init__(self, ten, tuoi, gioiTinh, diaChi, nganh):
        super().__init__(ten, tuoi, gioiTinh, diaChi)
        self.nganh = nganh

    def inTTin(self):
        super().inTTin()
        print("Ngành:", self.nganh)


class NhanVien(CanBo):
    def __init__(self, ten, tuoi, gioiTinh, diaChi, congViec):
        super().__init__(ten, tuoi, gioiTinh, diaChi)
        self.congViec = congViec

    def inTTin(self):
        super().inTTin()
        print("Công việc:", self.congViec)

class QLCB:
    def __init__(self):
        self.ds = []

    def them(self, cb):
        self.ds.append(cb)

    def timKiem(self, ten):
        for cb in self.ds:
            if cb.ten.lower() == ten.lower():
                cb.inTTin()

    def hienThi(self):
        for cb in self.ds:
            cb.inTTin()
            print("------")

ql = QLCB()

while True:
    print("\n===== MENU =====")
    print("1. Thêm cán bộ")
    print("2. Tìm kiếm theo tên")
    print("3. Hiển thị danh sách")
    print("4. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        loai = input("Loại (1-Công nhân, 2-Kỹ sư, 3-Nhân viên): ")

        ten = input("Tên: ")
        tuoi = input("Tuổi: ")
        gioiTinh = input("Giới tính: ")
        diaChi = input("Địa chỉ: ")

        if loai == "1":
            bac = input("Bậc (1-10): ")
            ql.them(CongNhan(ten, tuoi, gioiTinh, diaChi, bac))

        elif loai == "2":
            nganh = input("Ngành: ")
            ql.them(KySu(ten, tuoi, gioiTinh, diaChi, nganh))

        elif loai == "3":
            congViec = input("Công việc: ")
            ql.them(NhanVien(ten, tuoi, gioiTinh, diaChi, congViec))

    elif chon == "2":
        ten = input("Nhập tên cần tìm: ")
        ql.timKiem(ten)

    elif chon == "3":
        ql.hienThi()

    elif chon == "4":
        break
