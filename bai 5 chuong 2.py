import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b*b - 4*a*c

if a == 0:
    print("Day khong phai phuong trinh bac 2")
else:
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co nghiem kep:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phuong trinh co hai nghiem phan biet:", x1, "va", x2)