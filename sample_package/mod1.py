
from sample_package import NOT_FOUND_ERROR, MY_CONSTANT


def fun_mod_1(*args, **kwargs):
    print(NOT_FOUND_ERROR)
    return 'fun_mod_1'


def fun_mod_2(*args, **kwargs):
    print(MY_CONSTANT)
    return 'fun_mod_1'

