"""
From decorators.py
You can now use this new decorator in other files by doing a regular import
import: https://realpython.com/absolute-vs-relative-python-imports/
"""
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

"""
>>> say_whee()
Whee!
Whee!
"""