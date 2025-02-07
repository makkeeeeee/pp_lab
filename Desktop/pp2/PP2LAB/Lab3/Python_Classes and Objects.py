#Create a Class 
class Student:
    x=5

#Create an Object
p1 = Student()
print(p1.x)

#The __init__() Function 
class Student:#constructor 
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Student("Ali",23)
print(p1.name)
print(p1.age)


#The __str__() Function
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = Student("Ali",23)
print(p1)


#Object Methods 
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Student("Ali",23)
p1.myfunc()

#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

#Modify Object Properties
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Student("Ali",23)
p1.age = 24
print(p1.age)


#Delete Objects
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Student("Ali",23)
del p1
print(p1)
