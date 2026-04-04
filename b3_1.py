with open("demo_file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())