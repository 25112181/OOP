#Bai tap 1: Lop Nhan vien
class Nhanvien:
    LUONG_MAX = 50000000

    def __init__(self, ten, luongcoban, hesoluong):
        self._ten = ten
        self._luongcoban = luongcoban
        self._hesoluong = hesoluong

    #===== Getter =====
    def get_ten(self):
        return self._ten
    def get_luongcoban(self):
        return self._luongcoban
    def get_hesoluong(self):
        return self._hesoluong    
    
    #===== Setter =====
    def set_ten(self, ten):
        self._ten = ten
    def set_luongcoban(self, luong):
        if luong > 0:
            self.__luongcoban = luong 
    def set_hesoluong(self, heso):
        if heso > 0:
            self.__hesoluong = heso

#===== Tinh luong =====
    def tinh_luong(self):
        luong = self._luongcoban * self._hesoluong
        return luong

#===== Tang luong =====
    def tang_luong(self, delta):
        if self.tinh_luong() + delta <= Nhanvien.LUONG_MAX:
            self._luongcoban += delta / self._hesoluong
        else:
            print("Vuot qua luong toi da!")

#===== In thong tin =====
    def in_thongtin(self):
        print("Ten: ", self.get_ten())
        print("Luong co ban: ", self.get_luongcoban())
        print("He so luong: ", self.get_hesoluong())

nv = Nhanvien("Mp", 5000000, 2.5)
nv.in_thongtin()
nv.tang_luong(2000000)
nv.in_thongtin()                        