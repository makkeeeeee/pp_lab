#Tuple Methods
#Python has two built-in methods that you can use on tuples.
#Python 有两个内置的方法，您可以对元组使用它们。

#count()
#返回元组中指定值的数量。
#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index()
#返回元组中指定值的索引。
#Return the index of the first item with the value 8:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

