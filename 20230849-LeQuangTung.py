from abc import ABC, abstractmethod

# ===================== NGOẠI LỆ =====================

class LoiNhanVien(Exception):
    pass

class KhongTimThayNhanVien(LoiNhanVien):
    def __init__(self, ma_nv):
        super().__init__(f"Không tìm thấy nhân viên có ID: {ma_nv}")

class LoiLuong(LoiNhanVien):
    pass

class LoiTuoi(LoiNhanVien):
    pass

class LoiDuAn(LoiNhanVien):
    pass

class TrungMaNhanVien(LoiNhanVien):
    pass


# ===================== KIỂM TRA =====================

def kiem_tra_tuoi(tuoi):
    if tuoi < 18 or tuoi > 65:
        raise LoiTuoi("Tuổi phải từ 18 đến 65")

def kiem_tra_luong(luong):
    if luong <= 0:
        raise LoiLuong("Lương phải lớn hơn 0")

def kiem_tra_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")


# ===================== MÔ HÌNH =====================

class NhanVien(ABC):
    def __init__(self, ma_nv, ten, tuoi, email, luong):
        kiem_tra_tuoi(tuoi)
        kiem_tra_luong(luong)
        kiem_tra_email(email)

        self.ma_nv = ma_nv
        self.ten = ten
        self.tuoi = tuoi
        self.email = email
        self.luong = luong
        self.ds_du_an = []

    @abstractmethod
    def tinh_luong(self):
        pass

    def them_du_an(self, du_an):
        if len(self.ds_du_an) >= 5:
            raise LoiDuAn("Nhân viên đã có tối đa 5 dự án")
        self.ds_du_an.append(du_an)

    def __str__(self):
        return f"[{self.ma_nv}] {self.ten} | Lương: {self.tinh_luong()} | Dự án: {len(self.ds_du_an)}"


class QuanLy(NhanVien):
    def tinh_luong(self):
        return self.luong * 2


class LapTrinhVien(NhanVien):
    def tinh_luong(self):
        return self.luong * 1.5


class ThucTapSinh(NhanVien):
    def tinh_luong(self):
        return self.luong * 0.8


# ===================== DỊCH VỤ =====================

class CongTy:
    def __init__(self):
        self.ds_nhan_vien = {}

    def tao_ma_tu_dong(self):
        return f"NV{len(self.ds_nhan_vien) + 1}"

    def them_nhan_vien(self, nv):
        if nv.ma_nv in self.ds_nhan_vien:
            print("⚠ Trùng ID → Tự sinh ID mới")
            nv.ma_nv = self.tao_ma_tu_dong()
        self.ds_nhan_vien[nv.ma_nv] = nv

    def tim_nhan_vien(self, ma_nv):
        if ma_nv not in self.ds_nhan_vien:
            raise KhongTimThayNhanVien(ma_nv)
        return self.ds_nhan_vien[ma_nv]

    def xoa_nhan_vien(self, ma_nv):
        if ma_nv not in self.ds_nhan_vien:
            raise KhongTimThayNhanVien(ma_nv)
        del self.ds_nhan_vien[ma_nv]

    def hien_thi(self):
        if not self.ds_nhan_vien:
            raise IndexError("Chưa có dữ liệu")
        for nv in self.ds_nhan_vien.values():
            print(nv)


def tong_luong(cong_ty):
    return sum(nv.tinh_luong() for nv in cong_ty.ds_nhan_vien.values())


# ===================== MENU =====================

def tao_nhan_vien():
    while True:
        try:
            ma_nv = input("ID: ")
            ten = input("Tên: ")
            tuoi = int(input("Tuổi: "))
            email = input("Email: ")
            luong = float(input("Lương: "))

            print("1. Quản lý | 2. LTV | 3. Thực tập")
            loai = int(input("Chọn: "))

            if loai == 1:
                return QuanLy(ma_nv, ten, tuoi, email, luong)
            elif loai == 2:
                return LapTrinhVien(ma_nv, ten, tuoi, email, luong)
            elif loai == 3:
                return ThucTapSinh(ma_nv, ten, tuoi, email, luong)
            else:
                print("Sai loại!")

        except ValueError:
            print("❌ Nhập sai định dạng!")
        except LoiNhanVien as e:
            print("❌", e)


def main():
    cong_ty = CongTy()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm")
        print("2. Danh sách")
        print("3. Tìm")
        print("4. Xóa")
        print("5. Thêm dự án")
        print("6. Tổng lương")
        print("0. Thoát")

        try:
            chon = int(input("Chọn: "))

            if chon == 1:
                nv = tao_nhan_vien()
                cong_ty.them_nhan_vien(nv)

            elif chon == 2:
                cong_ty.hien_thi()

            elif chon == 3:
                ma = input("ID: ")
                print(cong_ty.tim_nhan_vien(ma))

            elif chon == 4:
                ma = input("ID: ")
                cong_ty.xoa_nhan_vien(ma)

            elif chon == 5:
                ma = input("ID: ")
                nv = cong_ty.tim_nhan_vien(ma)
                nv.them_du_an(input("Tên dự án: "))

            elif chon == 6:
                print("Tổng lương:", tong_luong(cong_ty))

            elif chon == 0:
                break

        except ValueError:
            print("❌ Nhập sai!")
        except LoiNhanVien as e:
            print("❌", e)
        except IndexError as e:
            print(e)


if __name__ == "__main__":
    main()