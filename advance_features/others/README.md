# Others

## List comprehensions
### What
- List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
### Syntax
- `newlist = [expression for item in iterable if condition == True]`
- Condition
    - The `condition` is like a filter that only accepts the items that valuate to `True`
        - Example: Only accept items that are not `apple`
            - `newlist = [x for x in fruits if x != "apple"]`
    - The condition is `optional` and can be `omitted`
        - Example: With no `if` statement
            - `newlist = [x for x in fruits]`
- Iterable
    - The `iterable` can be any iterable object, like a `list`, `tuple`, `set`,...
        - Example: You can use the `range()` function to create an iterable
            - `newlist = [x for x in range(10)]`
    - Same example, but with a condition
        - Example: Accept only numbers lower than 5
            - `newlist = [x for x in range(10) if x < 5]`
- Expression
    - The `expression` is the current item in the iteration, but it is also the `outcome`, which you can manipulate before it ends up like a list item in the new list
        - Example: Set the values in the new list to upper case
            - `newlist = [x.upper() for x in fruits] `
        - Example: You can set the outcome to whatever you like - Set all values in the new list to 'hello'
            - `newlist = ['hello' for x in fruits]`
    - The `expression` can also contain conditions, `not` like a filter, but as a way to `manipulate` the outcome
        - Example: Return "`orange`" instead of "`banana`":
            - `newlist = [x if x != "banana" else "orange" for x in fruits]`

    
## Collections Module
- `collections` is a module in the standard library that implements alternative container datatypes.
- Example: a `Counter` is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values
    - `counter.py`
- Example: A `defaultdict` is a subclass of dict, which allows to pass a factory used to create automatically a new value when a key is missing
    - `defaultdict.py`
- Example: The `defaultdict` can be used to create a tree data structure
    - `tree.py`

## Itertools Module
- `itertools` is a module in the standard library that allows you to `create` iterators for efficient looping
- Example: `permutations` allows you to `generate` all the `possible` ways of `ordering` a set of things
    - `permutations.py`
- Example: `combinations` generates all the `possible` ways of `selecting items` from a `collection`, such that (`unlike` permutations) the `order` does not matter
    - `combinations.py`
- Example: `itertools` also contains utility functions such as `chain`, which takes iterables and creates a new iterator that returns elements from the given iterables sequentially, as a single sequence
    - `chain.py`

## Functools Module
- The `functools` module provides a few `decorators`, such as `lru_cache` which can do what we just did: `memoization`. It saves recent calls to save time when a given function is called with the same arguments
- Example: `lru_cache.py`

## Packing / Unpacking
- The `*` operator, known as the `unpack` or `splat operator` allows very convenient transformations, going from `lists` or `tuples` to separate variables or arguments and conversely.
    - example: `extended_iterable_unpacking.py`

- When the `arguments` for your function are `already` in a `list` or in a `tuple`, you can `unpack` them using `*args` if it's a `list`, or `**kwargs` if that's a `dict`.
    - example: `unpacking_arguments.py`

- The `opposite` is also possible, you can `define` a function that will `pack` all the `arguments` in a single `tuple` and all the keyword arguments in a single `dict`.
    - example: `keyword_arguments.py`

## Context Managers
- Context managers are mainly used to properly `manage resources`. The most `common` use of a context manager is the opening of a `file`: `with open('workfile', 'r') as f:`
- a context manager is just a `class` that implements the methods `__enter__` and `__exit__`.
    - `context_manage.py`
- to use a `generator` function with a single `yield`, using the `@contextmanager` decorator
    - `context_manager_decorator.py`
    
## Paradigms
- Python supports three types of Programming paradigms
    - Object Oriented programming paradigms
    - Procedure Oriented programming paradigms
    - Functional programming paradigms

## RegEx

## References
- [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [W3Schools](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [collections](https://docs.python.org/3/library/collections.html)
- [Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
- [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [itertools](https://docs.python.org/3/library/itertools.html)
- [permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations)
- [chain](https://docs.python.org/3/library/itertools.html#itertools.chain)
- [functools](https://docs.python.org/3/library/functools.html)
- [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [context manager](https://docs.python.org/3/library/stdtypes.html#typecontextmanager)
- [@contextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)
- [programming paradigms in Python](https://www.geeksforgeeks.org/programming-paradigms-in-python/)