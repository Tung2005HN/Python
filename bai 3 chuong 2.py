import time

x = time.localtime()
year = x[0]   # Lấy năm hiện tại

birth = int(input("Nhập năm sinh: "))
age = year - birth

print(f"Năm sinh {birth}, vậy bạn {age} tuổi")