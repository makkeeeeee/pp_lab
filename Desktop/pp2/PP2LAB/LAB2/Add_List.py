#Add List Items
#To add an item to the end of the list, use the append() method:
#要在列表末尾添加一个项目，请使用 append() 方法：
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")#在列表的末尾添加“橙色”
print(thislist)

#To add an item at the specified index, use the insert() method.
#要在指定索引处添加项目，请使用 insert() 方法。
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#在索引 1 处插入“橙色”
print(thislist)

#extend () method
#To append elements from another list to the current list, use the extend() method.
#要将另一个列表的元素附加到当前列表，请使用 extend() 方法。
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)#将 tropical 添加到 thislist
print(thislist)

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#extend() 方法不需要附加列表，您可以添加任何可迭代对象（元组、集合、字典等）。
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)#将 thistuple 添加到 thislist
print(thislist)