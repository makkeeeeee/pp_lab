#Tuple
#Tuple 用于在单个变量中存储多个项目。
#Tuple 是 Python 中用于存储数据集合的 4 种内置数据类型之一，其他 3 种分别是 List、Set 和 Dictionary，它们都有不同的特性和用法。
#元组是一个有序且不可更改的集合。
#元组用圆括号书写。

thistuple = ("almaty", "dubai", "beijing")
print(thistuple)

#Tuple Items
#Tuple 项目可以使用index号来访问。
#index从 0 开始，所以第一个项目index为 0，第二个项目index为 1，以此类推。
#访问元组中的项目：
thistuple = ("almaty", "dubai", "beijing")
print(thistuple[1])

#有序-当我们说图元是有序的，这意味着项目有一个确定的顺序，并且该顺序不会改变。
#不可更改-元组是不可更改的，这意味着在创建元组后，我们不能更改、添加或删除项目。
#允许重复-由于元组是有索引的，因此它们可以有具有相同值的项

#tuple length
#要确定元组中的项目数，请使用len()方法：
thistuple = ("almaty", "dubai", "beijing")
print(len(thistuple))

#Create Tuple With One Item
#要创建只有一个项目的元组，您必须在项目后添加一个逗号。
thistuple = ("almaty",)
print(type(thistuple))

#NOT a tuple
#如果您在项目后添加一个逗号，则会创建一个元组。
thistuple = ("almaty")
print(type(thistuple))

#Tuple Items - Data Types
#元组中的项目可以是任何数据类型：
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#type()
#要确定项目的数据类型，请使用type()函数：
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
#要创建一个新的元组，我们可以使用tuple()构造函数：
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)