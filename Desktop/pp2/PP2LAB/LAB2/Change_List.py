#Change item values 
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"#将第二个项目更改为“黑醋栗”
print(thislist)

#Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]#将第二个项目到第三个项目更改为“黑醋栗”和“西瓜”
print(thislist)

#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]#将第二个项目替换为“黑醋栗”和“西瓜”
print(thislist)

#Insert Items
#To insert a list item, without replacing any of the existing values, we can use the insert() method.
#要插入一个新的列表项，而不替换任何现有值，我们可以使用 insert() 方法
#Insert the value "orange" as the second item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#在第二个项目后插入“橙色”
print(thislist)

