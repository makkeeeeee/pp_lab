import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net" 

pattern = r"([A-Za-z']+ ){2}([A-Za-z']+)" # our regex 
# matches group of 3 words

results = re.finditer(pattern, text_to_match)

# print(result) # list of tuples with strings or just strings

for result in results:
    print(result)
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))