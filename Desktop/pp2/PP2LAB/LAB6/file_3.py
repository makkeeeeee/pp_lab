import os

path = "./"  # current path

# 检查路径是否存在
if os.path.exists(path):
    print("path exist")
    # 提取文件名
    filename = os.path.basename(path)
    print("file name:", filename)
    # 提取目录部分
    directory = os.path.dirname(path)
    print("firesctory :", directory)
else:
    print("path does not exist")