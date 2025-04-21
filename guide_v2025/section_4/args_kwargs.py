# print(1, 2, 3, 4, 'hello', sep=':') # *args
# *args
def add(*args: int) -> int: # *numbers
    print(args) # tuple
    return sum(args)

print(add(1, 2, 3))

# keyword arguments
def greet(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f'{greeting} {person}{ending}')

greet('Hello', 'Bob', 'James', 'Maria', ending='!')

# **kwargs
def pin_position(**kwargs: int) -> None:
    print(kwargs)

pin_position(x=10, y=20)

# rules
def func(*args: str, **kwargs: int) -> None:
    print(args)
    print(kwargs)

func('a', 'b', a=1, b=2)

def func_has_position_args_before_args(default: int, *args: int, **kwargs: int) -> None:
    print(1)
    pass

# def func_has_position_args_after_kwargs(*args: str, **kwargs: int, default: int) -> None:
#     # error
#     pass

def func_not_position_arguments(*args: str, default: int, **kwargs: int) -> None:
    print(args)
    print(default)
    print(kwargs)

func_not_position_arguments('a', 'b', default=2, a=1, b=2)
# func_not_position_arguments('a', 'b', 2, a=1, b=2) # TypeError
# func_not_position_arguments('a', 'b', a=1, b=2, 2) # syntax error

# func_has_position_args_before_args(default=1, 1,2,3, x=1, y=2) # syntax error
