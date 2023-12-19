from uppercase_sentence import uppercase_decorator

def split_string(function):
    print("aaa")
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())