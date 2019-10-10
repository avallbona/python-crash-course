"""
tuples
"""

# empty tuple
print("-" * 20)
b = ()
print(b)
print(type(b))

b = (1, 2, 3, 4)

# simple tuple
a = ("a", "b", "c", "d", "e", "f", "g")
print(a)

# length
print(len(a))

# accessing an element
print(a[2])

# tuples are immutables
try:
    a[1] = "bbb"
except TypeError as e:
    # outputs "'tuple' object does not support item assignment"
    print(str(e))

# we can add tuples
c = a + b
print(c)

# repetition
print(b * 4)

# membership
print(1 in b)

# iteration
for x in b:
    print("element: {}".format(x))

# slices
print(b[1:])

# slices
print(b[-1])

# min
print(min(b))

# max
print(max(b))
