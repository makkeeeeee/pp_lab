#Python Loops
#Python has two primitive loop commands:
# 1.while loops
# 2.for loops

# 1.while Loops
# With the while loop we can execute a set of statements as long as a condition is true.
#通过 while 循环，只要条件为真，我们就可以执行一组语句。
# Print i as long as i is less than 6:
# 打印 i 直到 i 小于 6：
i = 1
while i < 6:
  print(i)
  i += 1


# 2.while loops
# With the break statement we can stop the loop even if the while condition is true:
#通过 break 语句，即使 while 条件为真，我们也可以停止循环：
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# 3.while loops
# With the continue statement we can stop the current iteration, and continue with the next:
#通过 continue 语句，我们可以停止当前迭代，并继续下一个迭代：
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# 4.while loops
# With the else statement we can run a block of code once when the condition no longer is true:
#通过 else 语句，我们可以运行一个代码块，当条件不再为真时：
i = 1
while i < 6:
  print(i)
  i += 1
else:
    print("i is no longer less than 6")