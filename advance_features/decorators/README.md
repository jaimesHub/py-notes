# Decorators

## What
- 
- A decorator is a `design pattern in Python` that allows a user to add `new functionality` to an `existing` object `without modifying` its `structure`.
- Decorators are usually called `before` the definition of a function you want to decorate.

## Where
- Function
- Class

## Which (prerequisites)

### 1. Assigning Functions to Variables
- Create a function that will add one to a number whenever it is called. 
- We'll then assign the function to a variable and use this variable to call the function.
- Example: `assign_functions_to_variables.py`

### 2. Defining Functions Inside other Functions
- This is `relevant` in creating and understanding decorators in Python.
- Example: `define_func_inside_other_func.py`

### 3. Passing Functions as Arguments to other Functions
- Functions can also be passed as parameters to other functions
- Example: `func_as_arg_of_other_func.py`

### 4. Functions Returning other Functions
- A function can also `generate` another function
- Example: `func_returns_other_func.py`

### 5. Nested Functions have access to the Enclosing Function's Variable Scope
- Python allows a nested function to access the `outer` scope of the enclosing function. 
- This is a `critical` concept in decorators -- this pattern is known as a `Closure`.
- Example: `nested_func_access_enclosing_func_variable_scope.py`

## How
- Practice 1: Creating a decorator
    - Create a simple decorator that will `convert a sentence to uppercase` 
    - by defining a `wrapper` inside an `enclosed` function.
    - similar to `the function inside another function`
    - example: `uppercase_sentence.py`
    - Python provides a much `easier` way for us to apply decorators.
    - We simply use the `@` symbol `before` the function we'd like to decorate. 
    - example: `decorating_uppercase_sentence.py`

- Practice 2: Applying Multiple Decorators to a Single Function
    - We can use `multiple decorators` to a single function.
    - The decorators will be applied in the `order` that we've called them.
    - Example: `define another decorator that splits the sentence into a list.`
    - File: `decorator_split_string.py`
    - The application of `decorators` is from the `bottom up`

- Practice 3: Accepting Arguments in Decorator Functions
    - Sometimes we might need to define a decorator that accepts `arguments`.
    - We achieve this by passing the arguments to the `wrapper` function. 
    - The `arguments` will then be passed to the function that is being decorated at call time.
    - Example: `decorator_with_arguments.py`

- Practice 4: Defining General Purpose Decorators
    - To define a general purpose decorator that can be applied to any function we use `*args` and `**kwargs`.
    - `*args` and `**kwargs` collect all `positional and keyword arguments` and `stores` them in the `*args and kwargs variables`.
    - `*args` and `**kwargs` allow us to pass as many arguments as we would like during function calls.
    - example: `a_decorator_passing_arbitrary_arguments.py`

- Practice 5: Passing Arguments to the Decorator
    - how we'd pass arguments to the decorator itself
        - example: `passing_args_to_decorator.py`
        - define a decorator maker that accepts arguments then define a decorator inside it.
        - define a wrapper function inside the decorator as we did earlier.

## Debugging Decorators
- Note: decorators wrap functions
- The original function name, its `docstring`, and parameter list are all hidden by the wrapper closure
    - when we try to access the `decorated_function_with_arguments` metadata, we'll see the wrapper closure's metadata.
    - This presents a `challenge` when debugging.
        - Example: `passing_args_to_decorator.py`
            - print(decorated_function_with_arguments.__name__) # wrapper
            - print(decorated_function_with_arguments.__doc__) # 'This is the wrapper function'
    - In order to solve this `challenge` Python provides a `functools.wraps` [Decorator](https://docs.python.org/3/library/functools.html#functools.wraps)
    - This decorator copies the lost metadata from the undecorated function to the decorated closure.
        - Example: `using_functools.py`
    - It is `advisable and good practice` to always use `functools.wraps` when `defining` decorators. 
    - It will save you a lot of headache in debugging.


## Summary
- Decorators dynamically `alter` the functionality of a `function, method, or class` without having to directly use subclasses or change the source code of the function being decorated.
    - In Python, functions are `first class objects` which means that functions in Pytho can be used or passed as argument
    - Properties of `first class functions`:
        - A function is an instance of the Object type.
        - You can store the function in a variable.
        - You can pass the function as a parameter to another function.
        - You can return the function from a function.
        - You can store them in data structures such as hash tables, lists, …

- Using decorators in Python also `ensures` that your code is `DRY` (Don't Repeat Yourself).

- Decorators have several use cases such as:
    - Authorization in Python frameworks
    - Logging
    - Measuring execution time
    - Synchronization

## Reference: 
- [Python Documentation](https://docs.python.org/3/library/functools.html#functools.wraps)
- [Datacamp Decorators](https://www.datacamp.com/tutorial/decorators-python)
- [Geeksforgeeks](https://www.geeksforgeeks.org/decorators-in-python/)
- [FCC Decorators](https://freecodecamp.org/news/python-decorators-explained/)
    - [Example code](./code/python_decorators_explained.py)