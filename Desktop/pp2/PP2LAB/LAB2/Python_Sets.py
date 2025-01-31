#Set
#集合是无序的，无重复的元素的集合。
#可以使用大括号{}创建集合，或者使用set()函数创建集合。
#创建一个集合：
thisset = {"a", "b", "c"}
print(thisset)
#注意：集合是无序的，无重复的元素的集合。
#注意：集合是无序的，因此无法确定项目的显示顺序

#集合项目
#集合项是无序的、不可更改的，并且不允许重复值。
#每次使用时，集合项都可能以不同的顺序出现，并且不能通过索引或键来引用。
#集合项是不可更改的，这意味着在创建集合后，我们不能更改这些项。
#一旦创建了集合，就不能更改其项目，但可以删除项目和添加新项目。



#Duplicates Not Allowed
#集合中的项目不允许重复。
#创建一个集合，其中包含重复的项目：
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#注意：集合中的项目不允许重复。


#True and 1 is same value
#false and 0 is same value
thisset = {"apple", "banana", "cherry", True,1,2}
print(thisset)


#Get the length of a set
#要获取集合中的项目数，请使用len()方法：
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#Set Items - Data Types
#集合项目可以是任何数据类型：
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

#type()
#要确定集合项目的数据类型，请使用type()方法：
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
#要创建一个新的空集合，请使用set()构造函数：
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

