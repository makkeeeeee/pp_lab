#Access Items
#您不能通过引用索引或键来访问集合中的项目。
#但是，您可以使用 for 循环遍历集合项，或者使用 in 关键字询问集合中是否存在指定值。
#Loop Through a Set
#您可以使用 for 循环遍历集合中的项目：
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


#Check if Item Exists
#要检查项目是否存在，请使用 in 关键字：
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Once a set is created, you cannot change its items, but you can add new items.
