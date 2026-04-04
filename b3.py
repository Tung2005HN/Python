with open("demo_file1.txt", "r", encoding="utf-8") as f:
    content = f.read()              # đọc toàn bộ file
    content = content.replace("\n", " ")  # thay xuống dòng bằng khoảng trắng
    print(content)