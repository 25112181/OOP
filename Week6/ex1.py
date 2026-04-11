#Bai tap 1: Refactor Quan li hang hoa
from abc import ABC, abstractmethod
from datetime import datetime
class HangHoa(ABC):
    def __init__(self, ten, gia):
        self._ten = ten
        self._gia = gia

    # property
    @property
    def ten(self):
        return self._ten

    @property
    def gia(self):
        return self._gia

    # abstract method
    @abstractmethod
    def tinh_tien(self):
        pass

    # in thông tin
    def __str__(self):
        return f"Ten: {self.ten}, Gia: {self.gia}"

    # so sánh bằng
    def __eq__(self, other):
        return self.gia == other.gia

    # so sánh nhỏ hơn
    def __lt__(self, other):
        return self.gia < other.gia


# ===== HÀNG ĐIỆN MÁY =====
class HangDienMay(HangHoa):
    def __init__(self, ten, gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(ten, gia)
        self.bao_hanh = bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def tinh_tien(self):
        return self.gia

    def __str__(self):
        return super().__str__() + f", Bao hanh: {self.bao_hanh} tháng"

class HangSanhSu(HangHoa):
    def __init__(self, ten, gia, chat_lieu):
        super().__init__(ten, gia)
        self.chat_lieu = chat_lieu

    def tinh_tien(self):
        return self.gia

    def __str__(self):
        return super().__str__() + f", Chat lieu: {self.chat_lieu}"

class HangThucPham(HangHoa):
    def __init__(self, ten, gia, ngay_sx, ngay_hh):
        super().__init__(ten, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hh = ngay_hh

    def tinh_tien(self):
        return self.gia

    def kiem_tra_het_han(self):
        today = datetime.now()
        return today > self.ngay_hh

    def __str__(self):
        return super().__str__() + f", HSD: {self.ngay_hh.strftime('%d/%m/%Y')}"

ds = []

h1 = HangDienMay("Tivi", 10000, 24, 220, 500)
h2 = HangSanhSu("Bat", 200, "Su")
h3 = HangThucPham("Sua", 50, datetime(2024, 1, 1), datetime(2024, 12, 1))

ds.append(h1)
ds.append(h2)
ds.append(h3)

for h in ds:
    print(h)
print("So sanh gia h1 va h2:", h1 == h2)
ds.sort()
print("\nSau khi sap xep theo gia:")
for h in ds:
    print(h)
