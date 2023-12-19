# from decorators import do_twice
"""
>>> hi_adam = return_greeting("Adam")
Creating greeting
Creating greeting
>>> print(hi_adam)
None
"""

"""
Because the do_twice_wrapper() doesn’t explicitly return a value, 
the call return_greeting("Adam") ended up returning None.
"""

from return_greeting_2 import do_twice
"""
To fix this, you need to make sure the wrapper function returns 
the return value of the decorated function.
"""

"""
>>> return_greeting("Adam")
Creating greeting
Creating greeting
'Hi Adam'
"""
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

