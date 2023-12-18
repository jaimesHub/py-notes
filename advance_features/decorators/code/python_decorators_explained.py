# How to Create Decorators

"""
We use decorators to add additional functionality to existing functions
"""

def add_one_decorator(func):
    def add_one():
        value = func()
        return value + 1
    
    return add_one

"""
Now, if we have a function that returns a number, 
we can use this decorator to add 1 to whatever value it outputs
"""

def example_function():
    return 1

final_value = add_one_decorator(example_function)
# print("Function in function: ", final_value())

"""
Instead of calling add_one_decorator(example_function),
we can use @ with the same value and to be much more efficient
"""

@add_one_decorator
def example_function_2():
    return 1

"""
This means that whenever we call the example_function_2(), 
we will essentially be calling the add_one() defined within the decorator (add_one_decorator)
"""

final_value_2 = example_function_2()
# print("Using decorator: ", final_value_2)

"""
How to pass Arguments with Decorators
When using decorators, we might also want the decorated function
to be able receive arguments when it is called from the wrapper function.
"""

# @add_one_decorator
# def add(a,b):
#     return a + b

# print(add(1,2)) # 3

"""
TypeError: add_one_decorator.<locals>.add_one() takes 0 positional arguments but 2 were given
Tt means that the wrapper function (add_one) doesn't take any arguments but we provided 2 arguments
"""
# add(1,2) # error

"""
To fix this, we need to pass down any arguments received from add_one to the decorated function when calling it
"""
def add_one_decorator_2(func):
    def add_one(*args, **kwargs):
        value = func(*args, **kwargs)
        return value + 1
    
    return add_one

@add_one_decorator_2
def add(a,b):
    return a + b

# print("Decorated function with args, kwargs: ", add(3,4)) # 8
"""Why are Decorators In Python Useful? (Use cases)"""

import logging
"""Logging
- When building larger apps, it is often helpful to have logs of what functions
were executed with information, such as what arguments were used, and what the function returned
during the application's runtime
- Troubleshooting & Debugging when things go wrong
- Logging can be useful for monitoring the status of you program
"""
def function_logger(func):
    """
    Whenever the add_one function runs, a new log will be appended to the main.log file
    """
    logging.basicConfig(level=logging.INFO, filename="main.log")

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} ran with positional arguments: {args} and keyword arguments: {kwargs}. Return value: {result}")
    
    return wrapper

@function_logger
def add_one_2(value):
    return value + 1

# print(add_one_2(1))

"""Caching
- Context: If we have an app that requires running the same function multiple times with the same arguments,
returning the same value, it can quickly become inefficient and thake up unnecessary resources.

- Solution: To prevent this, it can be useful to store the arguments used and the returned value of the function
any time it is called, and simply re-use the returned value if we have already called the function with the same arguments.

- Which: @lru_cache from functools module
"""

from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

