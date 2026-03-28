a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")