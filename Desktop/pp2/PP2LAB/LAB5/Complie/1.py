# compile 

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net" 

pattern = re.compile('John') 
# pattern now is a regex object 
#使用 re.compile() 函数将正则表达式模式 'John' 编译成一个 re.Pattern 对象，并将其赋值给变量 pattern。
print(type(pattern)) # re.Pattern 

result = pattern.match(text_to_match)

print(result) # match object 

print(result.group()) # print the match as a string 