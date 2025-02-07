#Array 
#An array is a special variable, which can hold more than one value at a time.数组是一种特殊的变量，可以同时保存多个值。

#If you have a list of items (a list of person), you can loop through the list and get each item.
#如果您有一个项目列表（人员列表），则可以循环访问列表并获取每个项目。

#Create an array containing car names:
#创建包含汽车名称的数组：
cars = ["Ford", "Volvo", "BMW"]

#Get the value of the first array item:
#获取第一个数组项的值：
x = cars[0]

#Modify the value of the first array item:
#修改第一个数组项的值：
cars[0] = "Toyota"

#The Length of an Array
#返回数组中的项目数：
x = len(cars)

#Looping Array Elements
#循环访问数组元素：
for x in cars:
  print(x)

#Adding Array Elements
#添加数组元素：
cars.append("Honda")

#Removing Array Elements
#删除数组元素：
cars.pop(1)

#The remove() method removes the specified item.
#remove()方法删除指定的项目。
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)