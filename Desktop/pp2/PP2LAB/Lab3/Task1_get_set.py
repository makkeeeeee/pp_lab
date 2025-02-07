#Task 1
class Input:
    def __init__(self):
        self.s= ""
    def getString(self):
        self.s=input()
    
    def printString(self):
        print(self.s.upper())

o = Input()
o.getString()
o.printString()



