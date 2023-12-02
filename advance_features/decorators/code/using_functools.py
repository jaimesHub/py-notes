import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        "wrapper func"
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "This will say hi"
    return "hello there"

print(say_hi())

# When we check the say_hi metadata, 
# we notice that it is now referring to the function's metadata 
# and not the wrapper's metadata.
print(say_hi.__name__)
print(say_hi.__doc__)