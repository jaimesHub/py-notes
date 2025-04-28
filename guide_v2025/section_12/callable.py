fruit: str = 'banana'
number: int = 10

def func() -> None:
    print('func() was called!')

print(callable(fruit))
print(callable(number))
print(callable(func))

print(callable(range))
print(callable(str))
