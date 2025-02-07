class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w =w
    def area(self):
        return self.l*self.w
    
#test rectangle 
r1 =Rectangle(3,4)
print(r1.area())

