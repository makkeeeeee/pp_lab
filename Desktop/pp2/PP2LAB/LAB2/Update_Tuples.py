#元组Tuple是不可更改的，也就是说，一旦创建了元组，就不能更改、添加或删除项目。

#一旦创建了元组，就不能更改其值。元组是不可更改的，也叫不可变的。
#但有一个解决方法。您可以将元组转换为列表，更改列表，然后再将列表转换回元组。

#Update
#元组是不可更改的，但我们可以通过更改列表来更改元
x = ["kbtu","sdu","kaznu","narxoz"]
y= list(x)
y[1]="Nu"
x=tuple(y)
print(y)


#Add Items
#由于元组是不可变的，因此没有内置的 append() 方法，但有其他方法可以向元组添加项目。
#1. 转换为列表： 就像改变元组的变通方法一样，你可以把它转换成列表，添加项目，然后再把它转换回元组。
#2. 使用 + 运算符： 您可以使用 + 运算符来添加项目。

#1. 转换为列表： 就像改变元组的变通方法一样，你可以把它转换成列表，添加项目，然后再把它转换回元组。
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


#2.要向元组添加项目，请使用 + 运算符：
thistuple = ("apple", "banana", "cherry")
thistuple = thistuple + ("orange",)
print(thistuple)

#创建只有一个项目的元组时，请记住在项目后面加上逗号，否则它将不会被识别为元组。
thistuple = ("apple",)
print(type(thistuple))


#remove item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


#错误示范：要删除元组中的项目，请使用del关键字
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists



