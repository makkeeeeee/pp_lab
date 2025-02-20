#Scope - area of visibiilty


#1. 局部作用域（Local Scope）
def my_func():
    x = 10# local variable
    print(x)

my_func()
#局部作用域是在函数内部创建的作用域。
#在函数内部定义的变量，其作用域仅限于该函数内部，
# 外部无法直接访问这些变量。

#2. 嵌套作用域（Nested Scope）
x =100 #global variable 

def my_func():
    print(x) # access to global variable 

my_func()
print(x)


#3. 全局作用域（Global Scope）
x=5
def change_x():
    x =10#this is a local variable ,not changed version of global x
    print("inside if th fucntion:",x)

change_x()
print("outside the function:",x)


#4. 内嵌作用域（Enclosing Scope）
def outer():
    x = "oter var"

    def inner():
        print(x) #access to the var form enclosing scope

    inner()

outer()

#this is the same as 3 but with inner function
def outer():
    x = 5

    def inner():
        x =10 # this is local var ,not channged var x
        print("inside inner:",x) 
    
    inner()
    print("inside outer",x)# 5 (outer x did not change)

outer()


#5. Nonlocal 作用域（Nonlocal Scope）
def outer():
    x = 5

    def inner():
        x =10 
        print("inside inner:",x) 
    
    inner()
    print("inside outer",x)# 10

outer()



#6. 内置作用域（Built-in Scope）
print(len([1,2,3,4]))
print(max(10,20,30))

max = 100 #now max is var ,but not a function
#print(max(10,20)) will be error max is not function no nore

del max # we delete var max , return access to the function max()

print(max(10,20))#20 
