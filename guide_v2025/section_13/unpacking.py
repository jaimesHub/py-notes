# a = 5
# b = 10

# multiple assigment
# a, b = 5, 10
# a, b = [5, 10]
# a, b = 'XY'

# print(a, b)

# a, *b, c = 'abcdef'
# print(a, b)

# *_, last = 'abcdef'
# print(last)
# print(_)

# how unpacking works
# def add(a: int, b: int) -> None:
#     # print(f'{a} + {b} = {a + b}')
#     print(f'{a + b = }')

# add(1, 2)
# numbers: dict[str, int] = {'a': 5, 'b': 10}
# add(**numbers) # unpack dictionary

numbers: list[int] = [1, 2, 3, 4, 5]
params: dict[str, str] = {'sep': '-', 'end': '.'}
print(*numbers)
print(**params)
print(*numbers, **params)
