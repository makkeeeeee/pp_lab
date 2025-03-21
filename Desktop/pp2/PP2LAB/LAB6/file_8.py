import os

file_path = "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB6/mytest.txt"

# 检查路径是否存在和访问权限
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("filr is deleted(文件已删除)")
    else:
        print("file can not write to delete (文件不可写，无法删除)")
else:
    print("filr is not here(文件不存在)")