import math

#Task 1 Convert degree to radian
degree = 15
radian = math.radians(degree)
print(f"output  radian is :{round(radian,6)}")


#Task 2 Calculate the area of a trapezoid
h = 5
b1 = 5
b2 = 6
area_trapezoid = ((b1 + b2)/2)*h
print("the expected output is :",area_trapezoid)

#Task 3 Calculate the area of a regular polygon
n = 4
s = 25
area_polygon = (n*s**2)/(4*math.tan(math.pi/n))
print("the expected output is :",round(area_polygon))

#Task 4 Calculate the area of a parallelogram
b = 5
h = 6
area_parallelogram = b*h
print("the expected output is :",float(area_parallelogram))

