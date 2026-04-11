#Bai tap 2 : Lop sieu nhan 
class Sieunhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
    def display(self):
        print("Bai tap 2 : Lop sieu nhan")
        print(f"Ten: {self.ten}, Vu khi: {self.vu_khi}, Mau sac: {self.mau_sac}")
    

# Tao 2 sieu nhan
# Sieu nhan 1
sieu_nhan_1 = Sieunhan("Sieu nhan Xanh", "Kiem", "Xanh")
sieu_nhan_1.display()
# Sieu nhan 2    
sieu_nhan_2 = Sieunhan("Sieu nhan Do", "Sung", "Do")
sieu_nhan_2.display()
