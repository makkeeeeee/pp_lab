import re 

text_to_match = "Python is fun python!" 

pattern = '[Pp]ython' # our regex 

results = re.finditer(pattern, text_to_match) 
print(results) # iterator with match object 

for result in results:
    print(result)

#re.finditer() 函数：返回一个迭代器，该迭代器会逐个产生匹配对象，
# 适合处理大量匹配结果的情况，避免一次性将所有匹配结果加载到内存中