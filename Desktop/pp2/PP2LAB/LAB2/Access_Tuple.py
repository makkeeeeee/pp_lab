#Access Tuple Items
#访问元组项目
#您可以使用索引号来访问元组中的项目。
#访问元组中的第一个项目：
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

#访问元组中的第二个项目：
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#访问元组中的第三个项目：
thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

#Negative Indexing
#负索引
#使用负索引从列表的末尾访问项目：
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#访问元组中的最后一个项目：
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
#范围索引
#您可以指定返回的项目的范围，通过在方括号中指定项目的索引范围来实现。
#返回列表中从第二个项目到第三个项目：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:3])

#返回列表中从第三个项目到第四个项目：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:4])

#返回列表中从第三个项目到最后一个项目：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
#负索引范围
#使用负索引从列表的末尾访问项目：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
#检查项目是否存在
#要检查项目是否存在，请使用 in 关键字：
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

