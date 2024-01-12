# Chapter 7: Functions as First-Class Objects

- Functions in Python are first-class objects
- What is `first-class object`?
    - Created at runtime
    - Assigned to a variable or element in a data structure
    - Passed as an argument to a function
    - Returned as the result of a function
- Examples of this concept: `Integers`, `strings`, and `dictionaries`, ...
- Shorthand for `functions as first-class objects`
- native coroutines and asynchronous generators are covered in [Chapter 21](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch21.html#async_ch)

## Treating a Function Like an Object
- `__doc__` is one of several attributes of function objects.
    - It is used to generate the help text of an object.
    - try: `help(factorial)`
- `factorial`, for example, is an instance of the function class.
- [Functional programming](https://en.wikipedia.org/wiki/Functional_programming)

## Higher-Order Functions
- A function that takes a function as an argument or returns a function as the result is a higher-order function.
- example: map(), sorted(), filter(), reduce(), apply()
- call a function with a dynamic set of arguments
    - fn(*args, **kwargs)

## Modern Replacements for map, filter, and reduce
- map() and filter() return generators - a form of iterator
- reduce() function is a `functools` module
    - `functools` module vs `built-in`
    - reducing built-ins: all(), any(), any()
- To use a higher-order function, sometimes it is convenient to create a small, . one-off function. -> anonymous functions exist

## Anonymous Functions