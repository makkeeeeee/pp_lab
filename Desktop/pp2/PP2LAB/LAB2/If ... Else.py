#Python Conditions and If statements

a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif- 表示 “如果前面的条件不为真，那么试试这个条件 ”的方式。
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else- 会捕捉前面条件没有捕捉到的任何内容
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else :
  print("b is not greater than a")


#Short Hand If
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")


#You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And- 所有条件为真
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Or- 只要有一个条件为真
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20.")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200
if b > a:
  pass
