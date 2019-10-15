"""
functions
"""


def demo(p1, p2):
    print("demo")
    print(p1, p2)


demo(1, 2)


def fun(*args):
    print("fun with undefined number of params")
    for arg in args:
        print(arg)


fun(1, 2, 3, 4)
fun(1)
print("=" * 20)


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


print("demo2")


def demo2(par2, par3, par1=1):
    print(par1, par2, par3)


demo2(3, 4)
demo2(par2="v2", par3="v3")
demo2(par1=33, par2="v2", par3="v3")


print("demo3")


def demo3(p1="a", p2=None):
    if p2 is None:
        p2 = []
    p2.append(p1)
    print(p1)
    print(p2)


demo3("b")
demo3("c")
