print(.1 + .2 == .3) # false
print(f'.1 + .2 = {.1 + .2}')

from math import isclose

# a: float = .999
# b: float = 1.000

# a: float = .9995
# b: float = .1000

# a: float = 91
# b: float = 100

# a: float = .9999
# b: float = 1.000

# a: float = 1.5
# b: float = 2.0

a: float = .1 + .2
b: float = .3

print(f'{a} == {b}? ', a == b)
print(f'{a} == {b}? ', isclose(a, b, abs_tol=.001))
print(f'{a} == {b}? ', isclose(a, b, abs_tol=.002))
print(f'{a} == {b}? ', isclose(a, b, rel_tol=.001))
print(f'{a} == {b}? ', isclose(a, b, rel_tol=.01, abs_tol=1))
print(f'{a} == {b}? ', isclose(a, b, rel_tol=.01, abs_tol=1))
print(f'{a} == {b}? ', isclose(a, b, rel_tol=.001))