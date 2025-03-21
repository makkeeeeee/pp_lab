
source_path = "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB6/source.txt"
target_path =  "/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB6/target.txt"

with open(source_path, "r") as source:
    with open(target_path, "w") as target:
        target.write(source.read())
print("filr text is cony(文件内容已复制)")