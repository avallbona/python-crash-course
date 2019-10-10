"""
lists
"""

# empty list
a = []
print(type(a))
print(a)

# simple list
a = [1, 2, 3, 4]
print(a)

# add element
a.append(5)
print(a)

# remove a value
a.remove(4)
print(a)

# remove from position
a.pop(2)
print(a)

# insert at position
a.insert(0, -1)
print(a)

# fusion lists
b = ["a", "b", "c"]
a.extend(b)
print(a)

# slices
print("-" * 20)
print(a[0:2])

# slices
print("-" * 20)
print(a)
print(a[3:])
print(a[-1])

# length
print(len(a))

a = [1, 2, 3, 4]
# membership
print(1 in a)

# min
print(min(a))

# max
print(max(a))

# iteration
for x in b:
    print("element: {}".format(x))

# iteration with enumerate
for i, x in enumerate("hello world!!!"):
    print("element: {} of {}".format(i, x))

# sorted
a3 = {5, 4, 1, 6, 7, 8, 11}
print(sorted(a3))
