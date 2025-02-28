
import re


# Task 1 .Match a string that has an 'a' followed by zero or more 'b's.
# 匹配 “a ”后跟 0 个或多个 “b ”的字符串。
def follow_a_b(text):
    pattern = r'ab*$'
    if re.match(pattern, text):
        return True
    else:
        return False


print(follow_a_b("ab"))#T
print(follow_a_b("a"))#T
print(follow_a_b("aw"))#F


# Task 2.Match a string that has an 'a' followed by two to three 'b's.
# 匹配 “a ”后跟 2 到 3 个 “b ”的字符串。
def follow_a_b23(text):
    pattern = r'ab{2,3}$'
    if re.match(pattern,text):
        return True
    else:
        return False
print(follow_a_b23("ab")) #F
print(follow_a_b23("abbb")) #T
print(follow_a_b23("abb")) #T
print(follow_a_b23("abbbbb")) #F


#Task 3.Find sequences of lowercase letters joined with an underscore.
# 找到由下划线连接的小写字母序列。
def find_seq_under(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern , text)

print(find_seq_under("a_b abbb"))



#Task 4.Find sequences of one uppercase letter followed by lowercase letters.
# 找到由一个大写字母后跟小写字母的序列。
def find_seq_under(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern ,text)

print(find_seq_under("Ab abbb"))



#Task 5.Match a string that has an 'a' followed by anything, ending in 'b'.
# 匹配 “a ”后跟任何内容，以 “b ”结尾的字符串。
def follow_a_b(text):
    pattern = r'ab$'
    if re.match(pattern , text):
        return True
    else:
        return False
print(follow_a_b("ab")) #T
print(follow_a_b("a")) #F
print(follow_a_b("ajf")) #F



#Task 6.Replace all occurrences of space, comma, or dot with a colon.
# 将空格、逗号或句点替换为冒号。
def replace(text):
    pattern = r'[ ,.]'
    return re.sub(pattern ,':' , text)
print(replace("a,b.c d"))




#Task 7.Convert snake case string to camel case string.
# 将蛇形字符串转换为驼峰字符串。
def snaek_to(text):
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
print(snaek_to("hi_my_name_is_mari"))#第一个下划线后的字母会完成大写形式


#Task 8.Split a string at uppercase letters.
# 将字符串在大写字母处拆分。
def split(text):
    return re.findall(r'[A-Z][^A-Z]*',text)
print(split("HelloWorldThisIsPython"))



#Task 9.Insert spaces between words starting with capital letters.
# 在以大写字母开头的单词之间插入空格。
def insert(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)
print(insert("HelloWorldThisIsPython"))




#Task 10.Convert a given camel case string to snake case.
# 将给定的驼峰字符串转换为蛇形字符串。
def camel_snake(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text).lower()
print(camel_snake("HelloWorldThisIsPython"))

