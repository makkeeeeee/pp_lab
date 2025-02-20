#JSON - javascript object notation 
#1. JSON 简介
#JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。
# 它采用键值对的方式来存储数据，常用于在不同编程语言和系统之间传递数据。

#2. json 模块概述
#json 是 Python 标准库中的一个模块，提供了将 Python 对象与 JSON 数据进行相互转换的功能。

#3. Python 对象转 JSON 数据
#json.dumps() 函数
#功能：将 Python 对象（如字典、列表等）转换为 JSON 格式的字符串。

#4. JSON 数据转 Python 对象
#json.loads() 函数
#功能：将 JSON 格式的字符串解析为 Python 对象。

import json
{
    "name":"Ali",
    "age":25,
    "city":"New York"
}

data = {
    "name":"Ali",
    "age":25,
    "city":"New York"
}

#python object to json 
data = {"name":"Ali","age":25,"city":"New York"}

json_date = json.dumps(data)
print(json_date)
print(type (json_date )) #<class 'str'>

#JSON to python object 
json_string = '{"name":"Ali","age":25,"city":"New York"}'

data = json.loads(json_string)
print(data)
print(type(data))#<class 'dict'>