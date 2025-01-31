# Remove() item
#要删除列表中的项目，请使用remove()方法：
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#要删除指定索引处的项目，请使用pop()方法：
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item
#要删除最后一个项目，请使用pop()方法不带索引：
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del keyword
#要删除列表中的项目，请使用del关键字：
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del keyword
#要删除列表中的all项目，也可以使用del，把所有的删除
thislist = ["apple", "banana", "cherry"]
del thislist

#clear() method
#要清空列表，请使用clear()方法：
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


