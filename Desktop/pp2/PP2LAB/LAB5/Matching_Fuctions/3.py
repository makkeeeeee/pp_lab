import re

text_to_match = "Python is fun,python!"
pattern = '[Pp]ython' # our regex [Pp] 是一个字符类，它表示匹配方括号内指定的任意一个字符
#即要么匹配大写的 P，要么匹配小写的 p。所以 [Pp]ython 这个模式可以匹配 Python 或者 python

result = re.findall(pattern,text_to_match)
#中查找所有与模式 pattern 匹配的子字符串，并将这些匹配结果以列表的形式返回

print(result)# print the list of the string element

# print(result.group()) # print the match as the string 



