def do_twice(func):
    """
    The wrapper_do_twice() inner function now accepts any number of arguments 
    and passes them on to the function it decorates. 
    Now both your say_whee() and greet() examples works
    """
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

"""
>>> say_whee()
Whee!
Whee!

>>> greet("World")
Hello World
Hello World
"""