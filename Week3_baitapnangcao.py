class NhanVien:
    LUONG_MAX = 50000000  

    def __init__(self, ten, luongCoBan, heSoLuong):
        self._ten = ten
        self._luongCoBan = luongCoBan
        self._heSoLuong = heSoLuong

    def get_ten(self):
        return self._ten

    def get_luongCoBan(self):
        return self._luongCoBan

    def get_heSoLuong(self):
        return self._heSoLuong

    def set_ten(self, ten):
        self._ten = ten

    def set_luongCoBan(self, luong):
        if luong > 0:
            self._luongCoBan = luong

    def set_heSoLuong(self, heso):
        if heso > 0:
            self._heSoLuong = heso

    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    def tangLuong(self, delta):
        luong_moi = self.tinhLuong() + delta
        if luong_moi <= NhanVien.LUONG_MAX:
            self._luongCoBan += delta / self._heSoLuong
            print("Tăng lương thành công")
        else:
            print("Vượt quá lương tối đa!")

    def inTTin(self):
        print("Tên:", self._ten)
        print("Lương cơ bản:", self._luongCoBan)
        print("Hệ số lương:", self._heSoLuong)
        print("Lương:", self.tinhLuong())

nv = NhanVien("An", 5000000, 2.5)
nv.inTTin()
print("Tăng lương...")
nv.tangLuong(2000000)
nv.inTTin()