"""
dictionaries
"""

# empty dictionary
a = {}
print(type(a))
print(a)

# create dict
b = {"k1": "v1", "k2": "v2", "k3": "v3"}
print(b)

# update
c = {}
c.update({"k4": "v4", "k5": "v5"})
print(c)

# update
b.update(c)
print(b)

# iterate
print("=" * 10)
for k in b:
    v = b.get(k)
    print(k, v)

# iterate
print("=" * 10)
for k, v in b.items():
    print(k, v)

# access
print(b.get("k2"))


# update value
print("=" * 10)
b["k2"] = "v2222"
for k, v in b.items():
    print(k, v)

print("=" * 10)
# add a key
b["k6"] = "value6"
for k, v in b.items():
    print(k, v)
