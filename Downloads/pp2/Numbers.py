#int ,float,complex
x=1 #int
y=2.8 #float
z=1j #complex

# int (整数，是一个不带小数、长度不限的正负整数)
x=1
y=372623628327
z=-34
print(type(x))
print(type(y))
print(type(z))

#float(浮点数，是一个带小数、长度不限的正负整数)
u=-3.44
print(type(u))

#complex(复数，是一个带有虚部的复数)
v=3+5j
print(type(v))

#Type conversition
x= 1
y=2.8
z=1j

#convert from int --- float
a = float(x)

#convert from float --- int
b = int(y)

#convert from int --- complex
c = complex(x) #cannot convert complex numbers into another number type

print(a)
print(b)
print(c)

#RANDOM NUMBER
import random
print (random.randrange(2,5))