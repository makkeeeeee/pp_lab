import re 

text_to_match = "Python is fun python!" 

pattern = 'python' # our regex 

result = re.search(pattern, text_to_match) #用于在整个string text_to_match 中搜索第一个与模式 pattern 匹配的位置
print(result) # match object 

print(result.group()) # print the match as the string 用于返回匹配到的字符串
