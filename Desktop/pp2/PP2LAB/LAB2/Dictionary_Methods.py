#Dictionary Methods
# 1.clear() 方法
# clear() 方法用于清空集合，它会移除集合中的所有元素。
x= {"a", "b", "c"}
x.clear()
print(x)
# 2.copy() 方法
# copy() 方法用于复制集合，它会返回一个新集合。
x = {"apple", "banana", "cherry"}
y = x.copy()
print(y)
# 3.fromkeys() 方法
# fromkeys() 方法用于创建一个新字典，其中包含指定键和值。
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
# 4.get() 方法
# get() 方法返回指定键的值。
x = {'name': 'John', 'age': 36}
x.get('age')
# 5.items() 方法
# items() 方法返回一个包含所有 (键, 值) 元组的列表。
x = {'name': 'John', 'age': 36}
x.items()
