# Iterator & Generators
## Objectives
- Define `Iterator` and `Iterable`
- Understand the `iter()` and `next()` methods
- Build our `own` for loop
- Define what `generators` are and `how` they can be used
- Compare `generator functions` and `generator expressions`
- Use `generators` to `pause` execution of `expensive` functions

## Iterators vs Iterables?
- `Iterator` - an object that can be iterated upon. An object which returns data, one element at a time when `next()` is called on it
    - `"HELLO"` is an `iterable`, but it is `not` an `itertator` because we can not call `next()`
- `Iterable` - an object which will return an `Iterator` when `iter()` is `called` on int
    - examples: "Hello", [1,2,3] are iterable
    - `iter("HELLO")` returns an `iterator`, then we can use `next()`
- Examples
```
In [1]: name = "Oprah"

In [2]: next(name)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[2], line 1
----> 1 next(name)

TypeError: 'str' object is not an iterator

In [3]: 

In [3]: iter(name)
Out[3]: <str_ascii_iterator at 0x10bd1b160>

In [4]: it = iter(name)

In [5]: it
Out[5]: <str_ascii_iterator at 0x10c155e10>
```
- The `for loop` parse the `iterable` string to `iterator`, then use `next()` to go through each item
- `next()`: when `next()` is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.
    - examples:
    ```
    In [4]: it = iter(name)

    In [5]: it
    Out[5]: <str_ascii_iterator at 0x10c155e10>

    In [6]: next(it)
    Out[6]: 'O'

    In [7]: next(it)
    Out[7]: 'p'

    In [8]: next(it)
    Out[8]: 'r'

    In [9]: next(it)
    Out[9]: 'a'

    In [10]: next(it)
    Out[10]: 'h'

    In [11]: next(it)
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    Cell In[11], line 1
    ----> 1 next(it)

    StopIteration: 
    ```

    - same with `lists`
    ```
    In [16]: next(nums)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[16], line 1
    ----> 1 next(nums)

    TypeError: 'list' object is not an iterator

    In [17]: nums = iter(nums)

    In [18]: nums
    Out[18]: <list_iterator at 0x10c0f34c0>

    In [19]: next(nums)
    Out[19]: 1

    In [20]: next(nums)
    Out[20]: 2

    In [21]: next(nums)
    Out[21]: 3

    In [22]: next(nums)
    Out[22]: 4

    In [23]: next(nums)
    Out[23]: 5

    In [24]: next(nums)
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    Cell In[24], line 1
    ----> 1 next(nums)

    StopIteration: 

    ```

## Writing Our Own Version of `for loops`
- [dunder methods](https://www.codecademy.com/resources/docs/python/dunder-methods)
- Example: `for.py`

## Writing a Custom Iterator
- Example: `custom_iterator.py`

## Making our Deck class Iterable
- Example: `deck.py`

## Introduction to Generators
- Generators are iterators (but `not every iterator is not a generator`)
- Generators can be `created` with `generator functions`
- Generator functions use the `yield` keyword
- Generators can be `created` with `generator expressions`

- Functions vs Generator Functions
    - Functions:
        - Uses `return` keyword
        - returns `once`
        - `when invoked`, returns the `return value`
    - Generator Functions:
        - Uses `yield` keyword
        - can yield `multiple` times
        - `when invoked`, returns a `generator`
- Example
    ```
    def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

    In [3]: for num in count_up_to(10):
    ...:     print(num)
    ...: 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

    In [4]: counter = count_up_to(5)

    In [5]: counter
    Out[5]: <generator object count_up_to at 0x108d8b040>

    In [6]: next(counter)
    Out[6]: 1

    In [7]: next(counter)
    Out[7]: 2

    In [8]: next(counter)
    Out[8]: 3

    In [9]: next(counter)
    Out[9]: 4

    In [10]: next(counter)
    Out[10]: 5

    In [11]: next(counter)
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    Cell In[11], line 1
    ----> 1 next(counter)

    StopIteration: 
    ```
- Example: `first_generator.py`
- Recap:
    - Generator is just a generator functions
    - It's just a way of making a iterator quickly
    - We don't have to raise StopIteration
    - help(generator_function)
    - type casting: list(counter)

## Assignment 1: Week Generator Exercise

## Assignment 2: yes_or_no

## Writing a Beat Making Generator
- Exhausting a Generator
    - Calling `next` on a generator with nothing left to yield will throw a `StopIteration` error
    - When we loop over a generator, the loop will stop before the `StopIteration` error gets thrown
- `infinite.py`

## Assignment 3: make_song

## Testing Memory Usage With Generators
- `fib.py`

## Assignment 4: get_multiples

## Assignment 5: get_unlimited_multiples

## Generator Expressions AND Speed Testing!
- Generator Expressions:
    - Example: `genex.py`
    - You can also create generators from `generator expressions`
    - Generator expressions look a lot like list comprehensions
    - Generator expressions use `()` instead of `[]`

- Generator expression vs a list comprehension
    - Example: `gen_expression_speed_test.py`
    - Example: `test.py`

- Why Generators?
    - Lazy Evaluation
        - Also called calculation on demand
        - Only compute values as needed
        - Can help improve performance of your code

## Recap
- Generators are iterators
- Generators can be created with generator function using the yield keyword
- Generators can be created with generator expressions
- Generators may or may not have terminating conditions
- Generators can provide memory saving
- Generators calculate values as they are needed

## References
- [Generator Expression](https://www.pythontutorial.net/advanced-python/python-generator-expressions/)
