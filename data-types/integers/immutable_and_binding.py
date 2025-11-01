a = 10
print(id(a)) # will refer to integer object for 10

b = 10
print(id(a)) # will cache 10 which is same object being refered to by a

c = b
print(id(c)) # same reference object

b = b + 2
print(id(b)) # creating new object to store result (12) and rebounding to b 


d = 12
print(id(d)) # caching available object