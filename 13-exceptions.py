"""
exceptions
"""
a = 0
try:
    a = 3 / 2
except (ZeroDivisionError, NameError) as e:
    print("errorrrr", str(e), type(e))

print(a)
