"""
functions
"""


def fun(*args):
    for arg in args:
        print(arg)


fun(1, 2, 3, 4)
fun(1)


def foo(*args, **kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print(k, "->", v)


# by position
foo(1)

# by name
foo(k2="valor k2")

params = {"k1": "v1", "k2": "v2"}

# params expansion
print("-" * 20)
foo(**params)


print("-" * 20)


# mixed
def faz(par1, *args, **kwargs):
    print("par1", par1)
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print(k, "->", v)


faz("hola", 1, 2, 3, k1="v1", k2="v2")
