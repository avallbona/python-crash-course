"""
sets
"""

# empty set
a = set()
print(type(a))
print(a)


# create set
b = {1, 2, 3, 4}
print(b)

# create set
c = set()
c.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
c.update(["a", "b", "c"])
print(c)


# add and preserves the unicity
a.add("a")
a.add("b")
a.add("c")
a.add("c")
a.add("c")
print(a)

# add list and another set
a.update([4, 5], {1, 6, 8})
print(a)

# discard
a.discard("a")
print(a)
a.discard("b")
print(a)
a.discard("c")
a.discard("c")  # not existing element but NOT giving an error
try:
    a.remove("c")  # not existing element but giving an error
except KeyError as e:
    print("error, not existing key: {}".format(str(e)))
print(a)

# remove all items
a.clear()
print(a)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# intersection
print(a.intersection(b))

# union
print(a.union(b))

# difference
print(a - b)
print(b - a)

# symetric difference
print(a ^ b)

# membership
print(1 in a)
print(5 in a)
print(1 in b)
print(5 in b)
print(5 not in b)

# max
print(max(a))

# min
print(min(a))

# length
print(len(a))

# sum
print(sum(a))

print("=" * 10)
# iteration
for value in a:
    print(value)
print("=" * 10)

# enumerate
print("pos", "value")
for i, value in enumerate(a):
    print(i, value)

a1 = {1, 2, 3, 4, 5}
a2 = {3, 4}

# is subset
print(a2.issubset(a1))

# is superset
print(a1.issuperset(a2))

# sorted
a3 = {5, 4, 1, 6, 7, 8, 11}
print(sorted(a3))
