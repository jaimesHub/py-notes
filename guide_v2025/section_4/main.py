# * & /

# def func(var_a: str, /, var_b: str, *, var_c: str) -> None:
#     ...

# what does slash (/) do ?
def func(var_a: str, /, var_b: str) -> None: # var_a is a positional arg
    # before the slash (/) we have to pass arg's value as a positional argument
    # after the slash (/) we can pass a value of either positional argument or a keyword argument
    print(var_a)
    print(var_b)

func('a', 'b') # ok: passed as positional args
# func(var_a='a', var_b='b') # not ok: TypeError that means everything in front of the slash must be passed in as a positional arg

func('a', 'b') # ok: positional args
func('a', var_b='b') # ok: keyword args

# the asterisk (*)
def func_2(var_a: str, *, var_b: str) -> None:
    # before the asterisk(*) we can pass keyword / positional args
    # after the asterisk (*) we have to pass keyword args
    print(var_a)
    print(var_b)

# func_2('a', 'b') # TypeError: forces everything after * to be passed as keyword args (must be)

# combination
def func_3(var_a: str, /, var_b: str, *, var_c: str) -> None:
    print(var_a)
    print(var_b)
    print(var_c)

func_3('a', 'b', var_c='c') # ok
func_3('a', var_b='b', var_c='c') # ok
