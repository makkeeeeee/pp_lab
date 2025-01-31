#For Loops
# for循环
#for 循环不需要事先设置索引变量。
for x in range(2):
    print(x)


#Looping Through a String
# for循环
#您可以遍历字符串中的每个字符：
for x in "banana":
    print(x)


#The break Statement
# break语句
#break 语句用于跳出循环。
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Exit the loop when x is "banana", but this time the break comes before the print:
#退出循环，当 x 为 "banana" 时。
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#The continue Statement
# continue语句
#continue 语句用于跳过当前迭代的剩余语句，然后继续下一迭代。
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#The range() Function
# range() 函数
#要返回数字序列，可以使用 range() 函数。
#range() 函数返回的是一个可迭代对象（类型是对象），它生成的是从 0 开始到指定数字之前的数字。
#range(6)，注意数字 6 不包括在序列中。
for x in range(6):
    print(x)

#range(2, 6)，注意数字 6 不包括在序列中。
for x in range(2, 6):
    print(x)

#range(2, 30, 3)，注意数字 30 不包括在序列中。
for x in range(2, 30, 3):
    print(x)




#Else in For Loop
# for循环中的else
#在 for 循环中，可以使用 else 关键字来执行循环之后的代码块：
for x in range(6):
    print(x)
else:
    print("Finally finished")

#The else block will NOT be executed if the loop is stopped by a break statement.
#如果循环被 break 语句终止，则不会执行 else 代码块。
for x in range(6):
    if x == 3: break
    print(x)


#Nested Loops
#嵌套循环
#您可以通过在 for 循环中嵌套一个或多个 for 循环来创建一个嵌套循环。
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#The pass Statement
# pass语句
# for 循环无法为空，但如果您在尝试执行循环时什么也不做，则可以使用 pass 语句：
for x in [0, 1, 2]:
    pass