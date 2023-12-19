"""
moving the decorator to its own module that can be used in many other functions (e.g. syntactic_sugar_2.py).
module: https://realpython.com/python-modules-packages/
"""

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice