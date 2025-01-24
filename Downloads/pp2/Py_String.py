#String is used in words
print("hi,KBTU")

#Quats inside in print
print("hi,'KBTU'") 
print('hi,"KBTU"')

# Wirte a variable
a= "KBTU"
print(a)

#Multiple variable
a="""Kjisiauhd,uhia,dhusa"""
print(a)

b='''Kjisiauhd,uhia,dhusa'''
print (b)

#String are Array
a ="KBTU"
print(a[1]) #remember that the first character has the position 0
#will be : B

#Loop -- String
for x in "KBTU":
    print(x) # 会一行一个字母的列出来

#String Length
a="KBTU"
print(len(a)) # 这是查看String的长度

#Check String
txt ="The best university in KZ"
print("KZ" in txt) # 如果有KZ 就会返回True

#使用 If 语句检查String是否存在
txt ="The best university in KZ"
if "KZ" in txt:
    print("yes,KZ is in txt")

#If not
txt ="The best university in KZ"
print("KBTU" not in txt)

#if
txt ="The best university in KZ"
if "KBTU" not in txt:
    print("no,KBTU is not in txt")

