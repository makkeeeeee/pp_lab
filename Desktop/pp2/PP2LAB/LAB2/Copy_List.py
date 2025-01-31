#Copy a List

#You can use the built-in List method copy() to copy a list.
#您可以使用内置的List方法copy()来复制列表。
#Make a copy of a list with the copy() method:
#使用copy()方法复制列表：
thislist = ["kbtu","sdu","kaznu","alfarabi"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
#另一种复制列表的方法是使用内置方法list()。
#Make a copy of a list with the list() method:
#使用list()方法复制列表：
thislist = ["kbtu","sdu","kaznu","alfarabi"]
mylist = list(thislist)
print(mylist)

#Use the slice Operator
#您还可以使用切片运算符创建列表的副本。
#Make a copy of a list with the slice Operator:
#使用切片运算符复制列表：
thislist = ["kbtu","sdu","kaznu","alfarabi"]
mylist = thislist[:]
print(mylist)