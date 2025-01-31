#Booelan values 
print(10>9)
print(10==9)
print(10<9)

#when you write the condition will reuturn the true and false 
a=8
b=4
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#evaluate values and variables 
print(bool("kbtu"))
print(bool(5))

x="kbtu"
y=5
print(bool(x))
print(bool(y))

# Most value are true 
#在 Python 中，几乎所有有内容的 value 都会被评估为True。具体来说：
#String：除了empty string ，任何string 都被视为True 。例如，'hello'是True，而''是False。
#数字：除了数字0，其他所有数字都被视为True。比如，5是True，0是False。
#集合类型：列表、元组、集合和字典，只要不是空的，都会被视为True。例如，[1, 2] （列表）、
# (3,) （元组）、{4, 5} （集合）、{'key': 'value'} （字典）都是True
# 而[]、()、{}（空集合或空字典）则是False。 这种特性在条件判断语句（如if语句）中经常用到。
bool("hi")
bool(15)
bool(["BYD","Tesla"])

print(bool(False))
print(bool({}))

#还有一个values或object的求值结果为 False
# 那就是如果你的object是由一个具有返回 0 或 False 的 __len__ function的class构成的
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


#create function that returns  a Boolean Vaue
def myFun():
    return True

print(myFun())

#you can 根据function 的Bool 答案执行代码：
def myFunction() :
  return True

if myFunction():
  print("HI!")
else:
  print("BYE!")


#isinstance() function
#可用于确定对象是否属于某种数据类型
x = 200
print(isinstance(x, int))

