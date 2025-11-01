# Unlike small integers, python does not cache floats, but it does reuse some constants like 0.0 internally

a = 1.5
b = 1.5

print(a is b) # implementation dependent 
print(id(a))
print(id(b))

# If both literals appear in the same code block, compiler constant folding might reuse them — but that’s an optimization, not a guarantee.1