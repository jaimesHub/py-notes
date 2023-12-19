# create a function that will add one to a number whenever it is called. 
# We'll then assign the function to a variable and use this variable to call the function.

def plus_one(number):
    return number + 1

# In Python, functions are first-class objects, 
# which means they can be assigned to variables just like any other value.
add_one = plus_one
print(add_one(5))