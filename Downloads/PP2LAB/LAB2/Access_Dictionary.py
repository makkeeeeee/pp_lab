#Accessing Items
#您可以通过引用方括号内的键名来访问字典中的项目：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
thisdict = {
    "brand": "LINING",
    "model": "Kl",
    "year": 1964
}
x = thisdict.get("model")
print(x)

#Get Keys
#您可以通过使用 keys() 方法来列出字典中的所有键名：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.keys()
print(x)

#键值列表是字典的一个视图，这意味着对字典所做的任何更改都会反映在键值列表中。
#Get Values
#您可以通过使用 values() 方法来列出字典中的所有值：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)


#example
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



#Get Items
#您可以通过使用 items() 方法来列出字典中的所有项目（键值对）：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

#检查项目是否存在
#要检查项目是否存在，请使用 in 关键字：
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")