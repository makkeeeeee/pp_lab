#Nested Dictionaries
# 字典可以包含其他字典，称为嵌套字典。
myfamily = {
  "child1" : {
    "name" : "Ali",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tomiris",
    "year" : 2007
  },
  "child3" : {
    "name" : "Laila",
    "year" : 2011
  }
}
print(myfamily)

# 字典也可以包含列表，称为嵌套列表。
myfamily = {
  "child1" : ["Ali", 2004],
  "child2" : ["Tomiris", 2007],
  "child3" : ["Laila", 2011]
}
print(myfamily)

# 字典也可以包含元组，称为嵌套元组。
myfamily = {
  "child1" : ("Ali", 2004),
  "child2" : ("Tomiris", 2007),
  "child3" : ("Laila", 2011)
}
print(myfamily)

#Access Items in Nested Dictionaries
# 要访问嵌套字典中的项目，您可以使用两个索引。
# 第一个索引是外部字典的键，第二个索引是内部字典的键。
# 请记住，内部字典是外部字典的值。
myfamily = {
    "child1" : {
        "name" : "Ali",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tomiris",
        "year" : 2007
    },
    "child3" : {
        "name" : "Laila",
        "year" : 2011
    }
}
print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
# 要循环访问嵌套字典中的项目，您可以使用嵌套的 for 循环。
myfamily = {
    "child1" : {
        "name" : "Ali",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tomiris",
        "year" : 2007
    },
    "child3" : {
        "name" : "Laila",
        "year" : 2011
    }
}
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
