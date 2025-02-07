#Function 
def fun():
    print("Hello World")
fun()

#Function with parametr
def our_function(fname):
    print(fname + " Refsnes")

our_function("Ali")
our_function("Laora")
our_function("NUr")

#Parameter 
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Ali", "Refsnes")


#Arbitrary Arguments, *args 
def my_function(*kids):
  print("The youngest child is " + kids[2])#第二个元素，也就是0，1，2

my_function("GUlim", "Aknur", "Shyngys")


#key = value syntax
def why_function(child3 ,child2 , child1 ):
   print("The youngest child is " + child3)

why_function(child1 = "A", child2 ="B", child3="C")


#任意关键字参数，**kwargs
#如果您不知道将有多少关键字参数传递到您的函数中，请在函数定义中的参数名称前添加两个星号：**。
#通过这种方式，函数将接收参数词典，并可以相应地访问项目：
def kbtu_function(**kid):
   print("His last name is "+ kid["lname"])

kbtu_function(fname = "Ali", lname = "BABA")

#default value  如果我们调用不带参数的函数，它将使用默认值
def kz_function(country = "China"):
  print("I am from " + country)

kz_function("Sweden")
kz_function("India")
kz_function()
kz_function("Brazil")


#Passing a List as an Argument 将列表作为参数传递
def kz_function(food):
  for x in food:
    print(x)

hot_food = ["Besbarmak", "Naryn", "Sorpa"]

kz_function(hot_food)


#Return Values 返回值
def kz_function(x):
  return 5 * x

print(kz_function(3))


#The pass Statement pass语句
#函数定义不能为空，但如果您认为它不应该有任何操作，但仍然需要函数，则可以使用pass语句：
def kz_function():
  pass

#Positional-Only Arguments 位置参数
#位置参数是您在函数调用中指定的参数。
#位置参数必须按顺序传递，因为位置参数是通过位置来识别的。
#要指定函数只能有位置参数，请在参数后添加 , /：
def kz_function(x, /):
  print(x)

kz_function(3)


#Keyword-Only Arguments 关键字参数
#关键字参数是您在函数调用中指定的参数。
#关键字参数必须按名称传递，因为关键字参数是通过名称来识别的。
#要指定函数只能有关键字参数，请在参数后添加 *：
def kz_function(*, x):
  print(x)

kz_function(x=3)

#Combine Positional-Only and Keyword-Only Arguments 组合位置参数和关键字参数
#您可以组合位置参数和关键字参数。
#要指定函数只能有位置参数，请在参数后添加 , /：
def kz_function(x, /, *, y):
  print(x+y)

kz_function(3,y=4)

#Recursion 递归
#Python 支持递归。您可以使用递归来定义在函数的定义中调用自己的函数。
#以下示例计算数字的阶乘：
def kz_function(k):
  if k > 1:
    return k * kz_function(k - 1)
  else:
    return 1
  
print(kz_function(4))