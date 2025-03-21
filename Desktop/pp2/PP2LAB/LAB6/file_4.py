
file_path = "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB6/example.txt"

# 计算行数
with open(file_path, "r") as file:
    lines = file.readlines()
    print("文件行数file line number :", len(lines))