#Dictionary
#字典用于存储键值对中的数据值。
#字典是一个有序*、可更改且不允许重复的集合。

# Dictionary Items
#字典项是键值对。
#键是唯一的。
#值可以是任何数据类型。
#键必须是不可变的，如字符串、数字或元组。
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#Duplicates Not Allowed
#字典中不允许重复的键。
#在下面的示例中，您将看到两个名为 "model" 的键：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)


#Dictionary Length
#要返回字典中的项目数，请使用 len() 方法：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))

#Dictionary Items - Data Types
#字典中的值可以是任何数据类型：
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}


#type()
#要确定字典中的值的数据类型，请使用 type() 方法：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))



#The dict() Constructor
#要创建一个新字典，请使用 dict() 构造函数：
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

