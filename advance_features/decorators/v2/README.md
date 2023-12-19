# v2: Primer on Python decorators
- What they are
    - a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
- How to create and use them

- Decorators provide a simple syntax for calling [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)

## Functions
- How function works?
    - Side effects: 
        - a function returns a value based on the given arguments
        - outputting something to the console (e.g. `print()`)
    
- To understand decorators, the `first` side effect is enough

### First-Class Objects
- Functions are `first-class objects`
    - It means that `functions can be passed around and used as arguments`
    - Likes `str, int, float, list, ...`
- Note:
    - `parameter` function is passed as a `reference` -> this function is not executed
    - `wrap` function with parentheses will be called

### Inner Functions
- It's possible to [define functions](https://realpython.com/defining-your-own-python-function/) *inside other functions*. They are called [https://realpython.com/inner-functions-what-are-they-good-for/](https://realpython.com/inner-functions-what-are-they-good-for/)

- The `order` in which the inner functions are defined does not matter

- They are treated as local scope variables

### Returning Functions From Functions
- We return a `reference` to the inner function (e.g. `inner_function`)
- `inner_function()` with parentheses refers to the result of evaluating the function

## Simple Decorators
- They are functions which just like any other object in Python
- Example: [example 1](./code/simple_decorators_1.py)
- The so-called decoration happens at the following line: `say_whee = my_decorator(say_whee)`
- Put simply: `decorators wrap a function, modifying its behavior.`
    - `wrapper()` is a regular Python function, the way a decorator modifies a function can change dynamically.
    - Example: [example 2](./code/simple_decorators_2.py)

### Syntactic Sugar
- Python allows you to use decorators in a simpler way with the `@` symbol, sometimes called the [pie](https://www.python.org/dev/peps/pep-0318/#background) syntax.
- Example: [example 3](./code/syntactic_sugar_1.py)

### Reusing Decorators
- Their purpose: easy reusability
- Pattern: You can name your inner function whatever you want, and a generic name like `wrapper()` is usually okay
- Example: 
    - [example 4](./code/decorators.py)
    - [example 5](./code/syntactic_sugar_2.py)

### Decorating Functions With Arguments
- Problem: [example 6](./code/decorating_w_args.py)
    - The problem is that the inner function `wrapper_do_twice()` does not take any arguments, but `name="World"` was passed to it.
- Solution: 
    - You could fix this by letting `wrapper_do_twice()` accept one argument, but then it would not work for the `say_whee()`function you created earlier.
    - use [*args and **kwargs](https://realpython.com/python-kwargs-and-args/) in the inner wrapper function.
- Example:
    - [example 7](./code/rewrite_decorators.py)

### Returning Values From Decorated Functions
- What happens to the return value of decorated functions?
    - Example: [example 8](./code/return_greeting_1.py)
    - Oops, our decorator `ate` the return value from the function
- Solution: To fix this, you need to make sure the `wrapper` function returns the return value of the decorated function.
    - Example:
        - [example 9](./code/return_greeting_2.py)
        - [example 10](./code/return_greeting_1.py)

### Who Are You, Really?
-  [Introspection](https://en.wikipedia.org/wiki/Type_introspection) is the ability of an object to know about its own attributes at runtime.
-  the [@functools.wraps](https://docs.python.org/library/functools.html#functools.wraps) decorator,

## A Few Real World Examples
- [Timing Functions](https://realpython.com/primer-on-python-decorators/#timing-functions)
- [Debugging Code](https://realpython.com/primer-on-python-decorators/#debugging-code)
- [Slowing Down Code](https://realpython.com/primer-on-python-decorators/#slowing-down-code)
- [Registering Plugins](https://realpython.com/primer-on-python-decorators/#registering-plugins)
- [Is the User Logged In?](https://realpython.com/primer-on-python-decorators/#is-the-user-logged-in)

## Fancy Decorators
- [Decorating Classes](https://realpython.com/primer-on-python-decorators/#decorating-classes)
- [Nesting Decorators](https://realpython.com/primer-on-python-decorators/#nesting-decorators)
- [Decorators With Arguments](https://realpython.com/primer-on-python-decorators/#decorators-with-arguments)
- [Both Please, But Never Mind the Bread](https://realpython.com/primer-on-python-decorators/#both-please-but-never-mind-the-bread)
- [Stateful Decorators](https://realpython.com/primer-on-python-decorators/#stateful-decorators)
- [Classes as Decorators](https://realpython.com/primer-on-python-decorators/#classes-as-decorators)

## More Real World Examples
- [See more](https://realpython.com/primer-on-python-decorators/#more-real-world-examples)

## Conclusion

## References
- [Primer on Python decorators](https://realpython.com/primer-on-python-decorators/)
- [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)
- [Examples](https://github.com/realpython/materials/tree/master/primer-on-python-decorators)
- [first-class objects](https://dbader.org/blog/python-first-class-functions)
- [define functions](https://realpython.com/defining-your-own-python-function/)
- [*args and **kwargs](https://realpython.com/python-kwargs-and-args/)
- [Introspection](https://en.wikipedia.org/wiki/Type_introspection)