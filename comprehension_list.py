def is_prime(value):
    primes = {1, 2, 3, 5, 7}
    return value in primes


print("lista")
some_list = [element + 5 for element in range(10) if is_prime(element)]
print(some_list)

print("diccionario")
results = {element: element + 5 for element in range(10) if is_prime(element)}
print(results)

print("diccionario2 refactored")
results2 = {element: element + 5 for element in range(10) if element in (1, 2, 3, 5, 7)}
print(results2)

print("generador")
some_list2 = (element + 5 for element in range(10) if is_prime(element))
print(type(some_list2))
print(some_list2)
# print(next(some_list2))
# print(next(some_list2))

# for it in some_list2:
#     print(it)

print(list(some_list2))

print("operaciones")


def apply_operation(left_operand, right_operand, operator):
    import operator as op

    operator_mapper = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
    try:
        return operator_mapper[operator](left_operand, right_operand)
    except KeyError:
        return "Unrecognized operation"


print(apply_operation(2, 3, "+"))
print(apply_operation(2, 3, "-"))
print(apply_operation(2, 3, "*"))
print(apply_operation(2, 3, "/"))
print(apply_operation(2, 3, "."))
