#Add Items
#要向集合添加项目，请使用 add() 方法：
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Update Items
#要向集合添加多个项目，请使用 update() 方法：
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#update() 方法中的对象不一定是集合，它可以是任何可迭代对象（元组、列表、字典等）。
#Add Any Iterable
#要向集合添加任何可迭代对象（列表、元组、集合等）中的所有项目，请使用 update() 方法：
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)