#Change Values]
#您可以通过为其分配新值来更改字典中的项目。
#Change Values
thisdict ={
    "brand" :"Tesla",
    "model" : "Model 3",
    "year ":"2020"
}
thisdict["year"] = 2018
print(thisdict)

#Update dictionary
#您可以使用 update() 方法将字典中的项目添加到另一个字典中。
thisdict ={
    "brand" :"Tesla",
    "model" : "Model 3",
    "year ":"2020"
}
thisdict.update({"color":"red"})
print(thisdict)