#append()
#要在列表的末尾添加新项目，请使用append()方法：
list1 = ["a", "b" , "c"]
list1.append("d")
print(list1)

#extend()
#要添加列表中存在的项目，请使用extend()方法：
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#insert()
#要在列表的特定索引处添加新项目，请使用insert()方法：
list1 = ["a", "b" , "c"]
list1.insert(1, "d")
print(list1)

#remove()
#要从列表中删除项目，请使用remove()方法：
list1 = ["a", "b" , "c"]
list1.remove("b")
print(list1)