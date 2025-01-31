#Copy a Dictionary
#您可以使用 copy() 方法复制字典。
thisdict = {
    "brand" :"Tesla",
    "model" : "Model 3",
    "year ":"2020"
}
mydict = thisdict.copy()
print(mydict)



#dict() 方法从键-值对序列中创建字典。
#注意：键必须是唯一的。
#使用 dict() 方法从键-值对序列中创建字典：
thisdict = {
    "brand" :"Tesla",
    "model" : "Model 3",
    "year ":"2020"
}
mydict = dict(thisdict)
print(mydict)