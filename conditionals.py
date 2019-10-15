"""
conditionals
"""

a = -1

if a > 1:
    print("a > 1")
elif a < 0:
    print("a < 0")
else:
    print("a is {}".format(a))

b = "ok" if a == 0 else "ko"
