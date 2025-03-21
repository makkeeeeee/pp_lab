# 生成文件
for letter in range(ord('A'), ord('Z') + 1):
    file_name = chr(letter) + ".txt"
    with open(file_name, "w") as file:
        file.write(f"This is file {chr(letter)}.txt")
print("26 个文件已生成")