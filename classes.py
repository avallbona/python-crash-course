class A:

    dummy = 123

    def __init__(self, name, a, b):
        self.a = a
        self.b = b
        self.name = name

    def sum_ab(self,):
        return self.a + self.b

    @staticmethod
    def sum(p1, p2):
        return p1 + p2

    @classmethod
    def demo(cls):
        return cls.__name__, cls.dummy

    def __repr__(self):
        return f"this is the representation of {self.name}, {self.a} and {self.b}"


op = A("pepe", 5, 4)


print("static method")
print(op.sum(7, 8))

print("instance method")
print(op.sum_ab())


print("class method")
print(A.demo())


class OneMixin:
    def product(self):
        return self.a * self.b


class B(A, OneMixin):
    pass


varb = B("manuel", 8, 5)

print("product")
print(varb.product())


print(op)

print(varb)
