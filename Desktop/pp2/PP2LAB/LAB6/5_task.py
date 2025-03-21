#Task 5 Check if all elements in a tuple are true(检查元组中的所有元素是否为真)

my_tuple = (True, 1, "hello", [1, 2])

if all(my_tuple):
    print("元组中的所有元素True")
else:
    print("元组中存在Fasle")