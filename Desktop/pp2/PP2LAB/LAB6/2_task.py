#Task 2 Count uppercase and lowercase letters in a string
#计算字符串中大写字母和小写字母的数量

text = "Hello World! This is a Test."
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase 数量:", upper_count)
print("lowercase 数量:", lower_count)