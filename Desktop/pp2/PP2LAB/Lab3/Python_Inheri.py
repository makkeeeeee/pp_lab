#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#Create a Parent Class
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("Mariya", "Saulesh")
x.printname()

#Create a child class that will inherit all the methods and properties from the parent class
class Student(Person):
    pass


#Use the Student class to create an object, and then execute the printname method:
x = Student("Make", "Ali")
x.printname()

#Add the __init__() function to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


#SUper 
#Use the super() function to refer to the parent class:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


#Add properties to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

#Add methods will also inherited for the child class
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

