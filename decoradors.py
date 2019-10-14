"""
decorators
"""

class decorator_class:
    def __init__(self, x):
        self.x = x

    def __call__(self, a):
        print("The square of", a, 'is')
        print(self.x(a))
        print('End')


@decorator_class
def square(value):
    return value ** 2


square(2)
