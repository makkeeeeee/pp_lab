#lambda arguments : expression

#A lambda function is a small anonymous function.lambda 函数是一个小型匿名函数
#A lambda function can take any number of arguments, but can only have one expression.lambda 函数可以接受任何数量的参数，但只能有一个表达式。

x =lambda a:a+10
print(x(5))


x= lambda a,b:a*b
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(5,6,2))


#why we need it ?
def ourfunction(n):
    return lambda a:a*n

#and we insert one number 
ourdouble = ourfunction(3)
ourtriple = ourfunction(4)
print(ourdouble(11))
print(ourtriple(11))



