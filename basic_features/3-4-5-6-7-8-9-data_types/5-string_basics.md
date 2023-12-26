# String Basics

## Introducing Strings
- Basic Data Types
- "STRINGS OF CHARACTERS"
- Strings are `a textual datatype` and must be `wrapped in quotes`
- ex: perl necklace
- ex: 
    - `color = "Magenta"`
    - `twitter_handle = '@POSTUS'`
    - `url = "www.reddit.com/r/formula1/"`
- IPython examples
    ```
        In [13]: "hello world"
        Out[13]: 'hello world'

        In [14]: 'Bye world'
        Out[14]: 'Bye world'

        In [15]: type("")
        Out[15]: str

        In [16]: type("hello")
        Out[16]: str

        In [17]: type("8")
        Out[17]: str

        In [18]: type(8)
        Out[18]: int
    ```
- Rules
    - `Good`: 'Hello World!', "Hello's World's"
    - `Invalid`: 'The cat's toy'

## String Variables
- Change type
```
age = 85
age = "eighty five"
```

## String Operators
- Concatenation: We can concatenate strings together by using the `plus` sign. No space will be added between them.
- Examples
    ```
    In [21]: "hello" + "world"
    Out[21]: 'helloworld'

    In [22]: "hello" + " world"
    Out[22]: 'hello world'

    In [23]: "hello" + " " + " world"
    Out[23]: 'hello  world'

    In [24]: last_name = "HorseLady"

    In [25]: first_name = "Tammy"

    In [26]: 

    In [26]: first_name + last_name
    Out[26]: 'TammyHorseLady'

    In [27]: first_name + " " + last_name
    Out[27]: 'Tammy HorseLady'

    In [28]: full_name = first_name + " " + last_name

    In [29]: full_name
    Out[29]: 'Tammy HorseLady'

    In [30]: "4" + "5"
    Out[30]: '45'

    In [31]: 4 + 5
    Out[31]: 9
    ```
- Multiplication: We can also multiply a string by a number, which will `repeat` that string
- Examples
    ```
    In [33]: 4 * 5
    Out[33]: 20

    In [34]: "hello" * "hi"
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[34], line 1
    ----> 1 "hello" * "hi"

    TypeError: can't multiply sequence by non-int of type 'str'

    In [35]: "ha" * 10
    Out[35]: 'hahahahahahahahahaha'

    In [36]: 3 * "hi"
    Out[36]: 'hihihi'

    In [37]: "hi" + 3
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[37], line 1
    ----> 1 "hi" + 3

    TypeError: can only concatenate str (not "int") to str
    ```

## String Indexing
- Strings Are `Ordered`
- Strings Are `Indexed`
- Indexes: it `starts` counting it `zero`
- Examples
    ```
    In [39]: "hello"[0]
    Out[39]: 'h'

    In [40]: "hello"[4]
    Out[40]: 'o'

    In [41]: first_name
    Out[41]: 'Tammy'

    In [42]: last_name
    Out[42]: 'HorseLady'

    In [43]: first_name[0]
    Out[43]: 'T'

    In [44]: last_name[0]
    Out[44]: 'H'

    In [46]: last_name
    Out[46]: 'HorseLady'

    In [47]: first_name[99]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    Cell In[47], line 1
    ----> 1 first_name[99]

    IndexError: string index out of range

    In [48]: 123[0]
    <>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
    <ipython-input-48-3f05973c2c95>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
    123[0]
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[48], line 1
    ----> 1 123[0]

    TypeError: 'int' object is not subscriptable
    ``` 
- We can use a `negative index` starting from the `end of the string` (the last character)
- Examples
    ```
    In [50]: first_name[-1]
    Out[50]: 'y'

    In [51]: first_name
    Out[51]: 'Tammy'
    ```

## The Special Value None
- `None` is a special value in Python that denotes the `lack of value`. It is `not` the same as `0` or an `empty string` (`those are still values`) ~ `NULL` value in JS
- It is `emptiness`, it means `nothing`
- It is very `different` from `0` or `an empty string`, those are still value

# References
- [Null in Python](https://realpython.com/null-in-python/)

