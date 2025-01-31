#Access list items
thislist= ["apple", "banana", "cherry"]
print(thislist[1])#第一个项目的index为 0

#Nagative indexing
thislist= ["apple", "banana", "cherry"]
print(thislist[-1])#最后一个项目的index为 -1

#Range of indexes
thislist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#返回第二个到第五个项目（不包括第五个项目）搜索将从索引 2（包含）开始，到索引 5（不包含）结束。

#By leaving out the start value, the range will start at the first item:
thislist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#返回第一个到第四个项目（不包括第四个项目）

#By leaving out the end value, the range will go on to the end of the list:
thislist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#返回第二个到最后一个项目（不包括最后一个项目）

#Range of Negative Indexes
thislist= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#返回第四个到最后一个项目（不包括最后一个项目）

#Check if Item Exists
thislist= ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

    


