#1. 删除文件
# 使用 os.remove() 函数删除文件。
# 在删除文件之前，可以使用 os.path.exists() 检查文件是否存在，避免报错。

import os

# 删除文件
if os.path.exists("demofile.txt"):  # 检查文件是否存在
    os.remove("demofile.txt")  # 删除文件
    print("文件已删除！")
else:
    print("文件不存在，无法删除。")


#2. 删除文件夹
# 使用 os.rmdir() 函数删除空文件夹。
# 注意：os.rmdir() 只能删除空文件夹。如果文件夹不为空，会报错。

import os

# 删除空文件夹
if os.path.exists("myfolder"):  # 检查文件夹是否存在
    os.rmdir("myfolder")  # 删除文件夹
    print("文件夹已删除！")
else:
    print("文件夹不存在，无法删除。")