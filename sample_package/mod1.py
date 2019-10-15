
from sample_package import NOT_FOUND_ERROR, MY_CONSTANT


def fun_mod_1(*args, **kwargs):
    print(NOT_FOUND_ERROR)
    return 'fun_mod_1'


def another_fun_mod_1(*args, **kwargs):
    print(MY_CONSTANT)
    return 'another_fun_mod_1'

def demo():
    return "this is demo from mod 1"