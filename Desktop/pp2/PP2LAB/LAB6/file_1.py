# 计算 example.txt 文件的行数
import os

path = "./"  # current path

# 列出所有目录 list the main catalog
print("directory(目录):")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

# 列出所有文件 list all file 
print("\nfile(文件):")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

# 列出所有目录和文件 all the file and catalog
print("\n所有目录和文件:")
for item in os.listdir(path):
    print(item)


