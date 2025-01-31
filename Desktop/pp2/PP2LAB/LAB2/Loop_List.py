# for loop
#You can loop through the list items by using a for loop:
# 您可以使用for循环遍历列表项：
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#You can also loop through the list items by referring to their index number.
#您还可以通过引用其索引编号来循环访问列表项。
#use range() and len() to create a suitable iterable
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Using while loop
#You can loop through the list items by using a while loop.
#您可以使用while循环遍历列表项。
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
#使用len()函数确定列表的长度，然后从0开始，通过引用其索引访问列表项。
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#列表简洁语法
#List comprehension 为您提供了一种更短的语法，当您要基于现有列表的值创建新列表时。
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]



