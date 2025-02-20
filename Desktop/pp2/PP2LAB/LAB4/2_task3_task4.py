#Task 3 用于迭代 0 到 n 范围内能同时被 3 和 4 整除的数字
def div_gene(n):
    for i in range (0,n+1):
        if i%3==0 and i%4==0:
            yield i

n=20
for num in div_gene(n):
    print(num)


#Task 4 用于生成从 a 到 b 的所有数字的平方，并使用 for 循环测试它，打印每个生成的值
def squares(a,b):
    for i in range (a,b+1):
        yield i **2

a = 1
b = 4
for square in squares(a,b):
    print(square)
