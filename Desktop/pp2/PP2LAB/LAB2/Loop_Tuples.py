#Loop Tuples
#您可以使用 for 循环来循环查看元组项
#Print all items in the tuple:
fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)


#Loop Through the Index Numbers
#您可以使用range()和len()函数来循环遍历元组索引
#Print all items by referring to their index number:
fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
  print(fruits[i])

#Using a While Loop
#您可以使用while循环来循环遍历元组索引
#Print all items, using a while loop to go through all the index numbers:
fruits = ("almaty", "beijing", "dubai")
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1