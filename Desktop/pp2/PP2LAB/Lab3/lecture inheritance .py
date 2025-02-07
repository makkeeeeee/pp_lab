class Person:
    def __init__(self,name,age):
        self.name=name
        self.age =age 

    
    def __str__(self):
        return f"{self.name}is {self.age}uears old"

class Student(Person):
    def __init__(self,name,age, id):
        super().__init__(name,age)
        self.id=id
    
    def __str__(self):
        return super().__str__() + f"with id {self.id}"
    
student1 = Student("Ali",98,"24B123456")

print(student1)