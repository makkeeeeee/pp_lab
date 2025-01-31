#Remove Set
#To remove an item in a set, use the remove(), or the discard() method.
#要删除集合中的项目，请使用 remove() 或 discard() 方法。
#Remove "banana":
thisset = {"chatgpt", "deepseak", "doubao"}
thisset.remove("chatgpt")
print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"chatgpt", "deepseak", "doubao"}
thisset.discard("chatgpt")
print(thisset)

#Note: If the item to remove does not exist, remove() will raise an error.
#注意：如果要删除的项目不存在，则 remove() 将引发错误。

#You can also use the pop(), method to remove an item,
# but this method will remove the last item. Remember that sets are unordered, 
# so you will not know what item that gets removed.
#您还可以使用 pop() 方法删除项目，但是此方法将删除最后一个项目。请记住，集合是无序的，因此您将不知道哪个项目被删除。
thisset= {"chatgpt", "deepseak", "doubao"}
x = thisset.pop()
print(x)

#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
#集合是无序的，因此使用 pop() 方法时，您不知道哪个项目被删除。

#The clear() method empties the set:
#clear() 方法清空集合：
thisset = {"chatgpt", "deepseak", "doubao"}
thisset.clear()
print(thisset)

