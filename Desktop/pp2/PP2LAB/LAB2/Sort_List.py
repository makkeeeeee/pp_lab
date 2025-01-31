#Sort List Alphanumerically
#按字母数字排序
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
#列表对象有一个sort()方法，它将按字母数字对列表进行排序，默认升序。
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)

#数字
thislist = [1, 5, 6, 2, 10]
thislist.sort()
print(thislist)

#Sort Descending
#降序
#To sort descending, use the keyword argument reverse = True:
#要降序排序，请使用关键字参数reverse = True：
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort(reverse = True)
print(thislist)

#数字
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Customize Sort Function
#自定义排序函数
#You can also customize your own function by using the keyword argument key = function.
#您还可以通过使用关键字参数key = function 自定义自己的函数。
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Case Insensitive Sort
#不区分大小写的排序
#By default the sort() method is case sensitive
# resulting in all capital letters being sorted before lower case letters:
#默认情况下，sort()方法是区分大小写的，因此所有大写字母在小写字母之前排序：
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#小写
#Luckily we can use built-in functions as key functions when sorting a list.
#幸运的是，当对列表进行排序时，我们可以使用内置函数作为关键函数。
#What if you want a case-insensitive sort?
#如果您想进行不区分大小写的排序，该怎么办？
#To ignore upper- and lowercase, you can use the lower() method to return a lower case version of the string:
#要忽略大小写，您可以使用lower()方法返回字符串的小写版本：
thislist = ["Kbtu", "sdu", "Alfarabi", "narxoz"]
thislist.sort(key = str.lower)
print(thislist)


#Reverse Order
#反向排序
#What if you want to reverse the order of a list, regardless of the alphabet?
#如果您想反转列表的顺序，无论字母顺序如何？
#The reverse() method reverses the current sorting order of the elements.
#reverse()方法反转元素的当前排序顺序。
thislist = ["Kbtu", "sdu", "Alfarabi", "narxoz"]
thislist.reverse()
print(thislist)

