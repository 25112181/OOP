#Bai tap 1 : He thong phan loai hang hoa 
class Hanghoa:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia

    def Tinh_tien(self):
        return self.gia

    def In_thong_tin(self):
        print("Ten hang: ", self.ten)
        print("Gia: ", self.gia)

class HangDienMay(Hanghoa):
    def __init__(self, ten, gia, baohanh, dienap, congsuat):
         super().__init__(ten, gia) 
         self.baohanh = baohanh
         self.dienap = dienap
         self.congsuat = congsuat
    def In_thong_tin(self):
        super().In_thong_tin()
        print("Thoi gian bao hanh: ", self.baohanh)
        print("Dien ap: ", self.dienap)
        print("Cong suat: ", self.congsuat)

class HangSanhSu(Hanghoa):
    def __init__(self, ten, gia, chatlieu, xuatxu):
        super().__init__(ten, gia)
        self.chat_lieu = chatlieu
        self.xuat_xu = xuatxu

    def In_thong_tin(self):
        super().In_thong_tin()
        print("Chat lieu: ", self.chat_lieu)
        print("Xuat xu: ", self.xuat_xu)

class HangThucPham(Hanghoa):
    def __init__(self, ten, gia, ngaysanxuat, ngayhethan):
        super().__init__(ten, gia)
        self.ngay_san_xuat = ngaysanxuat
        self.ngay_het_han = ngayhethan

    def In_thong_tin(self):
        super().In_thong_tin()
        print("Ngay san xuat: ", self.ngay_san_xuat)
        print("Ngay het han: ", self.ngay_het_han)

print("=== Hang Dien May ===")
dien_may = HangDienMay("Tu lanh", 50000000, "24 thang", "220V", "150W")        
dien_may.In_thong_tin()

print("\n=== Hang Sanh Su ===")
sanh_su = HangSanhSu("Ly", 100000, "Thuy tinh", "Viet Nam")
sanh_su.In_thong_tin()

print("\n=== Hang Thuc Pham ===")
thuc_pham = HangThucPham("Sua", 20000, "2026-04-01", "2026-12-03")
thuc_pham.In_thong_tin()
