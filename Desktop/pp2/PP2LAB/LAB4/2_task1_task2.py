#Task 1 用于生成直到某个数 N 的数字的平方
def square_generator(n):
    for i in range (n+1):
        yield i**2

n=4
for square in square_generator(n):
    print(square)


#Task 2 以逗号分隔的形式打印 0 到 n 之间的偶数，其中 n 从控制台输入
def even_gene(n):
    for i in range (0,n+1,2):
        yield i

n = int(input("Number:"))  
even_num = [str(num)for num in even_gene(n)]  
print(",".join(even_num))   



