#Slicing
b = "KBTU"
print(b[2:4])# Get the characters from position 2 to position 4 (not included也就是不包含4，但是包含2)

#Slice From the Start
b = "KBTU"
print(b[:4] ) # Get the characters from the start to position 4 (not included)

#Slice To the End
b = "KBTU"
print(b[2:]) # Get the characters from position 2, and all the way to the end

#Negative Indexing
b = "KBTU"
print(b[-4:-1]) # Get the characters from position -4 (included) to position -1 (not included)
#负索引 -5 指向的字符是 "World!" 中的 "o"。因为从右往左数，"d" 是 -1，"l" 是 -2，"r" 是 -3，"o" 是 -4，"W" 是 -5。
#负索引 -2 指向的字符是 "World!" 中的 "l"。
#切片操作 b[-5:-2] 表示从索引 -5 开始（包含该位置的字符），到索引 -2 结束（不包含该位置的字符）。所以会截取 "o"、"r" 和 "l" 这三个字符。
