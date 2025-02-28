import re
text_match_to = "Python is fun,python!"
pattern = "python" # our regex
result = re.match(pattern ,text_match_to)
#return none : no match form the beginnig of the string
# because the match() requries the match to happend at the begining of the string 
# use search() instead such cases

# print(result)#None
# print(result.group())#error 

