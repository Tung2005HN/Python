# Nhập thông tin
name = input("Tên: ")
age = input("Tuổi: ")
email = input("Email: ")
skype = input("Skype: ")
address = input("Địa chỉ: ")
work = input("Nơi làm việc: ")

# Lưu vào file
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\nTuổi: {age}\nEmail: {email}\nSkype: {skype}\nĐịa chỉ: {address}\nNơi làm việc: {work}")

# Đọc lại
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print("\nThông tin đã lưu:")
    print(f.read())