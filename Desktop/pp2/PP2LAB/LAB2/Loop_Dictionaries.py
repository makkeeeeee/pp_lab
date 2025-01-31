#Loop Through a Dictionary
#您可以使用 for 循环遍历字典中的项目：
thisdict={"brand":"Ford","model":"Mustang","year":1964}
for x in thisdict:
    print(x)


#您可以使用 values() 方法来返回值列表。
thisdict={"brand":"Ford","model":"Mustang","year":1964}

for x in thisdict.values():
    print(x)

#您可以使用 items() 方法来返回键-值对列表。
thisdict={"brand":"Ford","model":"Mustang","year":1964}

for x,y in thisdict.items():
    print(x,y)