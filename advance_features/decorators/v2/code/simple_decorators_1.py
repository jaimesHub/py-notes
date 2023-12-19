def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

"""
>>> say_whee
<function my_decorator.<locals>.wrapper at 0x7f3c5dfd42f0>
>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
"""