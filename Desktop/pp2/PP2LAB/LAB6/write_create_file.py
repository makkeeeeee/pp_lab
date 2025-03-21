#1. 写入现有文件: 
# 使用 "a" 模式追加内容到文件末尾。
# 使用 "w" 模式覆盖文件内容。

# 追加内容到文件
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")  # 追加内容
f.close()

# 读取并打印文件内容
f = open("demofile2.txt", "r")
print(f.read())  # 打印追加后的内容
f.close()

# 覆盖文件内容
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")  # 覆盖内容
f.close()

# 读取并打印文件内容
f = open("demofile3.txt", "r")
print(f.read())  # 打印覆盖后的内容
f.close()


#2. 创建新文件
# 使用 "x" 模式创建新文件（如果文件已存在会报错）。
# 使用 "w" 或 "a" 模式创建文件（如果文件不存在）。

# 使用 "x" 模式创建新文件
try:
    f = open("myfile.txt", "x")  # 创建新文件
    f.write("This is a new file!")  # 写入内容
    f.close()
except FileExistsError:
    print("文件已存在！")

# 使用 "w" 模式创建文件（如果文件不存在）
f = open("myfile.txt", "w")  # 如果文件不存在，会创建新文件
f.write("This is another new file!")  # 写入内容
f.close()

# 使用 "a" 模式创建文件（如果文件不存在）
f = open("myfile.txt", "a")  # 如果文件不存在，会创建新文件
f.write("\nThis line is appended!")  # 追加内容
f.close()