#Variables that are created outside of a function are known as global variables
#Global variables can be used by everyone, both inside of functions and outside.

#first example
x = "great"
def myfunc():
    print("Python is "+x)

myfunc()

#second example
#Create a variable inside a function, with the same name as the global variable
x= "SDU"

def myfunc():
    x="Kbtu "
    print("The best "+x)#the function will print the local variable

myfunc()#这里会输出：The best Kbtu
print("The best "+x)#这里会输出：The best SDU 



#Global Keyword-if I add the Global keyword ,the variable can be usd the out-intside of the function
def myfunc():
    global x
    x="BEST"

myfunc()

print("Kbtu is "+x)

#if I use diffrent variable for x , and the inside function add global keyword 
# the final output vairble is global variable
x="WHAT"
def myfunc():
    global x
    x="KBTU"

myfunc()
print("Best university is "+x)#only output : Best university is KBTU


