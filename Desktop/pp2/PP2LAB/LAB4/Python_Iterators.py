#iterators and gerators

#an  iterator is an object which contains number of values 
#and it can be iterated upon

our_list=[1,2,3]# Iterator

our_list_iter = iter(our_list) 

print(next(our_list_iter))# 1 使用 next() 函数从迭代器中获取下一个值
print(next(our_list_iter))# 2
print(next(our_list_iter))# 3

#print(next(our_list_iter))#StopIteration 出错，因为已经没有第四个数字了

#2
mystr = "hello"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#3
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



#4
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
            

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#7
def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

#print(next(gen))#Stopiterator

for i in my_generator():
    print(i)

def example():
    yield "hello"
    yield"world"

for i in example():
    print(i)