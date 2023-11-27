# Python Numbers

## Intro to Data Types
- Set of Data types example: Write Your Review Submition Template
- Data types
    - Strings
    - Integers
    - Frozenset
    - Booleans
    - Floats
    - Bytes
    - Dictionary
    - Complex
    - Range
    - List
    - Tuple
    - Set
- Basic data types: `Strings`, `Integers`, `Booleans`, `Floats`

## Integers and Floats
- There are 2 important `numeric types`: `Integers` and `floats`
- `Integers`
    - Whole numbers only
    - Positive or Negative
    - No decimal points
    - Example: 9, 378, -21
- `Floats`
    - Written With a Decimal Point
    - Positive or Negative
    - Example: 1.5, 9.99, -2.1
- Using ipython to realize difference
        - How: `type(variable)` tell us the type of that variable. 
        - e.g. type(6) -> int, type(5.6) -> float
        - it takes `more memory` to do math with `floats` versus `ints`
        - integers `are` actually `unbounded`. 
        - e.g. 35734890527432857431573445834290213462378493754
        - floats are `not` unbounded. e.g. 2.333333333333333333333333 -> 2.3333333333333335
        -> there is `a level of precision` that we run up agains with `floats`

## Numberic Notations
- `ints`: 
    - 31000000 or 31_000_000 `not` 31,000,000
    - 09 -> error
- `floats`: 
    - 1000.5 or 1_000.5 `not` 1,000.55
    - 1.234e12 `not` 1.234 e12
    - 6.7e-10, 6.7e-3

## Basic Operators
- Concepts
    - Operators are special characters in Python that perform operations on value(s).
- Example
    - Addition: 5 + 2, 5.4 + 2
    - Subtraction: 3 - 1, 4 - 1.0
    - Asterisk: 45 * 12
    - Division: 5 / 2, 10 / 2.6
- Order of Operations
    - Parentheses: `()`
    - Multiplication and Division: `*, /. //`
    - Addition anf Subtraction: `+, -`

## Lesser Known Operators
- Integer Division: `//`, it `rounds down` the result
- Exponentiation: `**`
- Modulo: `%`, remainders of ... , check even or odd numbers

## Python Comments
- Python will ignore any lines starting with the `#` symbol
- e.g. `# this never runs`