#Join Sets
#在 Python 中，有几种方法可以连接两个或多个集合。
# 1. union() 和 update() 方法可以连接两个集合中的所有项。
# 2.intersection() 方法只保留重复项。
# 3.difference() 方法保留第一个集合中不在另一个集合中的项。
# 4.symmetric_difference()方法会保留除重复项之外的所有项目。

# 1.union() 和 update() 方法
# union() 方法返回两个集合的并集。
# update() 方法在当前集合上修改，以包含两个集合中的所有项目。
# 注意：union() 和 update() 方法不会删除重复项。
# 1.union() 方法
# 返回两个集合的并集：
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
#可以使用 | 运算符代替 union() 方法，得到的结果是一样的。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)

# 2.update() 方法
# 在当前集合上修改，以包含两个集合中的所有项目
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

# 2.intersection() 方法
# intersection() 方法返回两个集合的交集。
# 注意：intersection() 方法不会删除重复项。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#可以使用 & 运算符代替 intersection() 方法，得到的结果是一样的。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x & y
print(z)
#intersection_update() 方法也只能保留重复数据，但它会更改原始数据集，而不是返回一个新的数据集。
x = {"a", "b", "c"}
y = {"google", "microsoft", "a"}
x.intersection_update(y)
print(x)
#True 和 1 被视为相同的值。False 和 0 也是如此。
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# 3.difference() 方法
# difference() 方法返回两个集合的差集。
# 注意：difference() 方法不会删除重复项。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)#x里的不同的列出来

#可以使用 - 运算符代替 difference() 方法，得到的结果是一样的。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x - y
print(z)

#difference_update()
#difference_update() 方法也只能保留重复数据，但它会更改原始数据集，而不是返回一个新的数据集。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)



# 4.symmetric_difference() 方法
# symmetric_difference() 方法返回两个集合的对称差集。
# 注意：symmetric_difference() 方法不会删除重复项。
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)#x和y里不同的列出来