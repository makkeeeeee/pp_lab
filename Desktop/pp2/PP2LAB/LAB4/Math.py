import math

print(math.floor(2.9))#2
print(math.ceil(2.9))#3

print(round(2.9))#3
print(round(2.10))#2

print(math.pow(2,3))#8
print(3**2)#9

print(math.sqrt(16))#4

def ath_root(x,n):
    return x**(1/n)
print(ath_root(16,2))#4

print(math.log(10)) # 2.302585092994046
print(math.log2(8)) # 3
print(math.log(100,10)) # 2

print(math.sin(math.radians(30))) # 0.5
print(math.cos(math.radians(60))) # 0.5
print(math.tan(math.radians(45))) # 1.0

print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
