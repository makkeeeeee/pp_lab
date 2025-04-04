#1. 文件处理的重要性
#文件处理是 Web 应用程序的重要组成部分。
#Python 提供了创建、读取、更新和删除文件的功能。

#2. open() 函数
#用于打开文件，是文件处理的核心函数。
#接受两个参数：文件名 和 模式。

#3. 文件打开模式
#"r" - 读取模式：默认模式，打开文件进行读取。如果文件不存在，会抛出错误。
#"a" - 追加模式：打开文件进行追加，文件指针位于文件末尾。如果文件不存在，会创建新文件。
#"w" - 写入模式：打开文件进行写入，会覆盖文件内容。如果文件不存在，会创建新文件。
#"x" - 创建模式：创建新文件，如果文件已存在，会抛出错误。

#4. 文件类型模式
#"t" - 文本模式：默认模式，文件以文本形式处理。
#"b" - 二进制模式：文件以二进制形式处理，适用于图片等非文本文件。

#5. 语法示例
#打开文件进行读取：
#python
#复制
f = open("demofile.txt")#等同于：python复制
f = open("demofile.txt", "rt")
#"r"（读取）和 "t"（文本）是默认值，无需显式指定。

#6. 注意事项
#确保文件存在，否则会抛出错误。使用 with 语句可以自动处理文件的关闭，避免资源泄漏：
with open("demofile.txt", "r") as f:
    content = f.read()
#文件操作完成后，务必使用 close() 关闭文件（除非使用 with 语句）。