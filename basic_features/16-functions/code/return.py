def divide(a, b):
    if b == 0:
        return "DON'T DIVIDE BY ZERO!"
    else:
        return a/b # Ends the execution of a function
    print("Hello")
    return (a//b)


# res = divide(1,3) # we can store in a variable

def scream(word):
    # While this function does print out a string,
    # it does not return anything
    # The default return value is NONE
    print(word.upper() + '!!!')

scream("I hate you")