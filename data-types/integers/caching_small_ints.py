a = 100
b = 100

print(a is b) # True, cached, always same object (within cache range)

x = 1000
y = 1000

print(x is y) # maybe False; maybe True, caching is not guaranteed

