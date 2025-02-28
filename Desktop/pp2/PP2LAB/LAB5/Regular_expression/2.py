#raw string

python_str = 'hello\n'
#hello and new line aafter hello 先是hello 然后换行

raw_str = r"hello\n"
#源自面上的字符串 就是hello\n 没有转义字符

print(python_str)
print(raw_str)


python_str = 'abc123\\'
raw_str = r'abc123\\'

print(python_str)
print(raw_str)

python_str = 'abc123\\\\'
raw_str = r'abc123\\\\'

print(python_str) # 两个\\ 代表一个\
print(raw_str)