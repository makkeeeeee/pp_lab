#Join two list
#在 Python 中，有几种方法可以连接或串联两个或多个列表。
#最简单的方法之一是使用 + 运算符。
#连接两个列表：
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#另一种连接两个列表的方法是将 list2 中的所有项目逐个追加到 list1 中：
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#can use the extend() method
#使用 extend() 方法，您可以添加列表中存在的项目：
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)