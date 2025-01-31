#Set Methods

#Add Items
#使用 add() 方法添加新项目。
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add Sets
#使用 update() 方法将一个集合添加到另一个集合中。
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)