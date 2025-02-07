class Shape:
    def A(self):
        return 0

class Square(Shape):
    def __init__(self,l):#constructor 
        self.l = l #l is length 
    def A(self):
        return self.l*self.l

    
#test Square
s1 =Square(5)
print(s1.A())




