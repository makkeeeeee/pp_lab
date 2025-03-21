import os

path = "./test.txt"


if os.path.exists(path):
    print("path exist")
    if os.access(path, os.R_OK):
        print("can read")
    else:
        print("can not read")
    # 检查可写性
    if os.access(path, os.W_OK):
        print("can write")
    else:
        print("can not write")
   
    if os.access(path, os.X_OK):
        print("can execute")
    else:
        print("can not execute")
else:
    print("path does not exist")