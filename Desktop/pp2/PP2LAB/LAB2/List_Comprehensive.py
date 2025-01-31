#List Comprehension
#当您想根据现有列表的值创建一个新列表时，列表理解提供了一种更简短的语法。
#例如,基于一个水果列表，您想创建一个新list，其中只包含名称中含有字母 “a ”的水果。
#如果没有列表理解功能，您就必须编写一个包含条件测试的 for 语句：
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)#只会列出单词里包含a 的单词

#使用列表理解，您可以编写更简短的代码。
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

#您也可以使用条件语句来过滤列表中的项目。
#在下面的示例中，我们将创建一个新列表，其中只包含名称中含有字母 “a ”的水果。
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]#只接受非 “苹果 ”产品

print(newlist)

#条件 if x != “apple ”将对除 “apple ”以外的所有元素返回 True，从而使新列表包含除 “apple ”以外的所有水果。
#条件是可选的，可以省略：
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print(newlist)

#Iterable 
#The iterable can be any iterable object, like a list, tuple, set etc.
#可迭代的
#You can also use the range() function to create an iterable:
#您还可以使用range()函数创建可迭代的对象：
newlist = [x for x in range(10)]
print (newlist)

#Accept only numbers lower than 5
newlist=[x for x in range(10)if x <5]
print(newlist)


#Expression
#表达式是迭代中的当前项，但也是结果，您可以在它最终成为新列表中的列表项之前对其进行操作：
newlist = [x.upper() for x in fruits]
print(newlist)

#The expression can also contain conditions
# not like a filter, but as a way to manipulate the outcome:
#表达式也可以包含条件
#与过滤器不同，但作为操作结果的方法：
newlist = ['hello' for x in fruits]
print(newlist)
