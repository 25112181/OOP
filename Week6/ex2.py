#Bai tap 2: Nang cap quan li can bo
from abc import ABC, abstractmethod
class TuoiKhongHopLe(Exception):
    pass
class BacKhongHopLe(Exception):
    pass
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
    @property
    def tuoi(self):
        return self._tuoi

    @tuoi.setter
    def tuoi(self, value):
        if value < 18 or value > 65:
            raise TuoiKhongHopLe("Tuổi phải từ 18-65")
        self._tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return f"{self.ho_ten} | {self.tuoi} tuổi | {self.gioi_tinh} | {self.dia_chi}"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        return self.ho_ten == other.ho_ten and self.tuoi == other.tuoi
    def __lt__(self, other):
        return self.ho_ten < other.ho_ten
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self):
        return self._bac
    @bac.setter
    def bac(self, value):
        if value < 1 or value > 10:
            raise BacKhongHopLe("Bậc phải từ 1-10")
        self._bac = value
    def mo_ta(self):
        return f"Công nhân bậc {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh
    def mo_ta(self):
        return f"Kỹ sư ngành {self.nganh}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def mo_ta(self):
        return f"Nhân viên làm {self.cong_viec}"

class QLCB:
    def __init__(self):
        self.ds = []

    def them(self):
        loai = input("Chọn loại (1-CN, 2-KS, 3-NV): ")
        try:
            ten = input("Tên: ")
            tuoi = int(input("Tuổi: "))
            gt = input("Giới tính: ")
            dc = input("Địa chỉ: ")

            if loai == "1":
                bac = int(input("Bậc (1-10): "))
                cb = CongNhan(ten, tuoi, gt, dc, bac)

            elif loai == "2":
                nganh = input("Ngành: ")
                cb = KySu(ten, tuoi, gt, dc, nganh)

            elif loai == "3":
                cv = input("Công việc: ")
                cb = NhanVien(ten, tuoi, gt, dc, cv)
            else:
                print("Chọn sai!")
                return
            self.ds.append(cb)
            print(">> Thêm thành công!")
        except Exception as e:
            print("Lỗi:", e)

    def hien_thi(self):
        if len(self.ds) == 0:
            print("Danh sách rỗng")
        for cb in self.ds:
            print(cb, "-", cb.mo_ta())

    def tim_kiem(self):
        ten = input("Nhập tên cần tìm: ")
        for cb in self.ds:
            if ten.lower() in cb.ho_ten.lower():
                print(cb, "-", cb.mo_ta())

    def luu_file(self):
        with open("canbo.txt", "w", encoding="utf-8") as f:
            for cb in self.ds:
                f.write(str(cb) + "\n")

    def doc_file(self):
        try:
            with open("canbo.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except:
            print("Chưa có file!")

ql = QLCB()

while True:
    print("\n===== MENU =====")
    print("1. Thêm cán bộ")
    print("2. Hiển thị")
    print("3. Tìm kiếm")
    print("4. Lưu file")
    print("5. Đọc file")
    print("0. Thoát")

    chon = input("Chọn: ")
    if chon == "1":
        ql.them()
    elif chon == "2":
        ql.hien_thi()
    elif chon == "3":
        ql.tim_kiem()
    elif chon == "4":
        ql.luu_file()
    elif chon == "5":
        ql.doc_file()
    elif chon == "0":
        break
    else:
        print("Chọn sai!")
