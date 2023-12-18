# Python Generators
- We learn about Python generators and how to use generators to create iterators

## Introduction to Python Generators
- Example: [regular_function.py](./code/regular_function.py)
- To `pause` a function `midway` and `resume` from `where` the function was paused, you use the `yield` statement.
- A generator is a function that contains at least one `yield` statement.
    - When you call a generator function, it `returns` a new generator object. 
    - it `doesn’t` start the function.
    - Generator objects (or `generators`) implement the [iterator protocol](https://www.pythontutorial.net/advanced-python/python-iterators/)
        - To execute a generator function, you call the `next()` built-in function on it.
- a generator object is also an [iterator](https://www.pythontutorial.net/advanced-python/python-iterators/), which must contain 2 dunder methods
    - `__iter__`
    - `__next__`

## A simple Python generator example
- Example: [generator_example.py](./code/generator_example.py)
- The `yield` statement is like a `return` statement in a function.
- Big difference
    - When Python `encounters` the `yield` statement, it `returns` the value specified in the `yield`. In addition, it `pauses` the `execution` of the function.
    - If you `call` the `same` function `again`, Python will `resume` from where the `previous yield` statement was encountered.
- To actually `execute` the body of a generator function, you need to use the `next()` built-in function
- `StopIteration` exception

## Using Python generators to create iterators
- Example: [squares.py](./code/squares.py)
    - The following example defines an `iterator` that returns a square number of an integer.
    - We use `the Squares iterator` to generate the square numbers of the first 5 integers from 0 to 5
    - We can rewrite `the Squares iterator` as `a generator function`

## Recap
- Python generators are functions that contain at least one yield statement.
- A generator function returns a generator object.
- A generator object is an iterator. Therefore, it becomes exhausted once there’s no remaining item to return.

# Python Generator Expressions
- We learn about the Python generator expression to create a generator object.

## Introduction to generator expressions
- Example: [generator_function.py](./code/generator_function.py)
- A generator expression is an `expression` that returns a `generator` object.
- Instead of using a `function` to define a generator function, you can use a `generator expression`
- A generator expression is like a list comprehension in terms of `syntax`. It supports
    - if statements
    - Multiple nested loops
    - Nested comprehensions
- A generator expression uses the parentheses `()` instead of square brackets `[]`.

## Generator expressions vs list comprehensions
- Example: [generator_expression.py](./code/generator_expression.py)
- Syntax
    - In terms of syntax, a generator expression uses parentheses `()` while a list comprehension uses the square brackets `[]`.

- Memory utilization
    - A list comprehension returns a list while a generator expression returns a generator object.
        - It means that a list comprehension returns a complete list of elements upfront. However, a generator expression returns a list of elements, `one at a time`, based on request.
    - A list comprehension is `eager` while a generator expression is `lazy`.
    - A list comprehension creates all elements `right away` and loads `all` of them into the `memory`.
    - A generator expression creates `a single element` based on request. It loads only one `single` element to the `memory`.
- Iterable vs iterator
    - A list comprehension returns an `iterable`. 
        - It means that you can iterate over the result of a list comprehension again and again.

    - A generator expression returns an `iterator`, specifically a lazy iterator. 
        - It becomes exhausting when you complete iterating over it.

## Recap
- Use a Python generator expression to return a generator.

# References
- [Python Generators](https://www.pythontutorial.net/advanced-python/python-generators/)
- [Python Generator Expressions](https://www.pythontutorial.net/advanced-python/python-generator-expressions/)
- [Wiki Python Generators](https://wiki.python.org/moin/Generators)