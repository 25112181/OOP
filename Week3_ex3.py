#Bai tap 3: Quan ly sieu nhan
class Sieunhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

ds_sieu_nhan = []

while True:
    ten = input("Nhap ten sieu nhan (hoac 'exit' de thoat): ")
    if ten == "exit":
        break

    vu_khi = input("Vu khi cua sieu nhan: ")
    mau_sac = input("Mau sac cua sieu nhan: ")
    
    ds_sieu_nhan.append(Sieunhan(ten, vu_khi, mau_sac))

print("Danh sach sieu nhan: ")
for sieu_nhan in ds_sieu_nhan:    
     print(f"Ten: {sieu_nhan.ten}, Vu khi: {sieu_nhan.vu_khi}, Mau sac: {sieu_nhan.mau_sac}")