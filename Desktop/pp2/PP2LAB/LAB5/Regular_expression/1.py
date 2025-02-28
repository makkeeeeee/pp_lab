#what is regular expressions
#RegEx或正则表达式是形成搜索模式的字符序列。
#RegEx可用于检查String是否包含指定的搜索模式。

import re 
text_to_match = "Python is fun!"
pattern = "Python"#our regex
result = re.match(pattern , text_to_match)

print(result)# match object

print(result.group()) #print the string of match 
