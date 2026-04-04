# Đọc file
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Tách từ
words = text.split()

# Đếm
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)