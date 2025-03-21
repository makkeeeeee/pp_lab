my_list = ["Apple", "Banana", "KBTU"]

file_path = "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB6/example.txt"

# 将列表写入文件
with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n")
print("List already write in file(列表已写入文件):", file_path)