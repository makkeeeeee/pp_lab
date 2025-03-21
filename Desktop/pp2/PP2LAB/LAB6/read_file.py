# 打开位于同一文件夹中的文件
f = open("demofile.txt", "r")
print(f.read())  # 读取并打印整个文件内容
f.close()

# 打开位于不同路径的文件
f = open("D:\\myfiles\\welcome.txt", "r")
print(f.read())  # 读取并打印整个文件内容
f.close()

# 读取文件的前 5 个字符
f = open("demofile.txt", "r")
print(f.read(5))  # 读取并打印前 5 个字符
f.close()

# 逐行读取文件
f = open("demofile.txt", "r")
print(f.readline())  # 读取并打印第一行
print(f.readline())  # 读取并打印第二行
f.close()

# 使用循环逐行读取整个文件
f = open("demofile.txt", "r")
for x in f:
    print(x)  # 逐行打印文件内容
f.close()

# 关闭文件（重要！）
f = open("demofile.txt", "r")
print(f.readline())  # 读取并打印第一行
f.close()  # 关闭文件