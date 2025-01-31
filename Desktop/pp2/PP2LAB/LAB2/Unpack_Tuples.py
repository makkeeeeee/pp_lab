#Unpacking a Tuple
#当您创建一个元组时，Python 会自动将其解包为多个变量。
#创建一个元组，并将其分配给多个变量：
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)


#注意：变量的个数必须与元组中值的个数一致，如果不一致，则必须使用星号将剩余的值作为一个列表收集起来。
#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)

#如果星号被添加到另一个变量名而不是最后一个变量名上，Python 将给该变量赋值，直到剩下的值的个数与剩下的变量个数相匹配。
#Using Asterisk*
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(tropic)#只会剩下中间的

