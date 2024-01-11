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