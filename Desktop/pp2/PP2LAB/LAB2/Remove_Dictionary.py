#Removing Items
#pop() 用于移除集合中的指定元素。
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")
print(thisdict)

#popitem() 用于移除集合中的最后一个元素（即键-值对）。
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()
print(thisdict)

#del 用于删除整个集合。
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#clear() 方法用于移除集合中的所有元素（键-值对）。
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)
