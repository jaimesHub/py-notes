# Booleans

## Introducing Booleans
- How we actually use booleans
- Where they come into play
- In the world of Python is around making decisions and comparisons and logic
    - `Decision Making`
        - Every single decision that any program makes is broken down into a series of `yes` or `no` decisions, `true` or `false` decisions
    - Example: Is the user logged in ? if Yes ... if No ...
    - Example: On / Off
- 2 possible values: `True` and `False`
    - Only the captialization
    - Example
    ```
        In [217]: False
        Out[217]: False

        In [218]: false
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        Cell In[218], line 1
        ----> 1 false

        NameError: name 'false' is not defined

        In [219]: True
        Out[219]: True

        In [220]: true
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        Cell In[220], line 1
        ----> 1 true

        NameError: name 'true' is not defined

        In [221]: type(True)
        Out[221]: bool

        In [222]: type("True")
        Out[222]: str
    ```
    
## Comparison Operators
- Operators are special characters in Python that perform operations on value(s)
- Comparisions Operators: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Examples: `>`, `<`, `>=`, `<=`
    ```
    In [224]: 3 > 10
    Out[224]: False

    In [225]: 30 > 10
    Out[225]: True

    In [226]: age = 19

    In [227]: age > 21
    Out[227]: False

    In [228]: age < 21
    Out[228]: True

    In [229]: balance = -1.99

    In [230]: balance > 100
    Out[230]: False

    In [231]: balance < 0
    Out[231]: True

    In [232]: age >= 21
    Out[232]: False

    In [233]: 30 >= 21
    Out[233]: True

    In [234]: 21 >= 21
    Out[234]: True

    In [235]: 21 > = 21
    Cell In[235], line 1
        21 > = 21
            ^
    SyntaxError: invalid syntax


    In [236]: 0 <= 10
    Out[236]: True

    In [237]: 0 <= 0
    Out[237]: True

    In [238]: 0 <= -99
    Out[238]: False

    In [239]: balance
    Out[239]: -1.99

    In [240]: balance > 0
    Out[240]: False
    ```
## Equality Operators
- Examples: `==`
    ```
    In [242]: 12 == 3
    Out[242]: False

    In [243]: 13 == 13
    Out[243]: True

    In [244]: 'a' == 'a'
    Out[244]: True

    In [245]: 'a' == 'A'
    Out[245]: False

    In [246]: 'hello' == 'hello'
    Out[246]: True

    In [247]: 'Hello' == 'hello'
    Out[247]: False
    ```
- Examples: `!=`
    ```
    In [249]: 1 != 2
    Out[249]: True

    In [250]: 1 != 1
    Out[250]: False

    In [251]: 1 == 1
    Out[251]: True

    In [252]: True == True
    Out[252]: True

    In [253]: False == False
    Out[253]: True

    In [254]: True == False
    Out[254]: False

    In [255]: 3.5 == 3.5
    Out[255]: True

    In [256]: 5.9 != 6.7
    Out[256]: True

    In [257]: 'hello' != 'bye'
    Out[257]: True
    ```
- Identity
    - `is`: Evaluates to True if a and b both refer to the same object in memory
    - `is not`: Evaluates to True if a and b do NOT refer to the same object in memory

## Comparing Across Types
    ```
    In [259]: 4.0 == 4
    Out[259]: True

    In [260]: 4.0001 == 4
    Out[260]: False

    In [261]: -3 == -3.0
    Out[261]: True

    In [262]: '4' == 4
    Out[262]: False

    In [263]: int('4') == 4
    Out[263]: True
    ```

## Truthiness & Falseyness
- Every value is inherently `Truth-y` or `False-y` in Python
- Falsey:
    - False, 0.0, 0
    - None, range(0)
    - Empty Strings: '', "", '''''', """"""
    - Empty Data Structures: [], (), {}, set()
- Truthy:
    - Everything else!
- `bool()`
    - We can use `bool()` to cast a value to a Boolean
    - This is one way to determine whether Python considers a value to be Truth-y or False-y

## The "in" Operator
- The `in` operator looks to see `if an item is a member of a sequence`.
- Example
    ```
    In [275]: "A" in "abba"
    Out[275]: False

    In [276]: "a" in "abAb"
    Out[276]: True

    In [277]: "bb" in "abbA"
    Out[277]: True

    In [278]: "bbb" in "abbA"
    Out[278]: False

    In [279]: 3 in 312
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[279], line 1
    ----> 1 3 in 312

    TypeError: argument of type 'int' is not iterable

    In [280]: 4 in [4, 5, 22]
    Out[280]: True

    In [281]: 43 in [4, 5, 22]
    Out[281]: False
    ```

## Comparing Strings
- Examples:
    ```
    In [283]: 'a' == 'a'
    Out[283]: True

    In [284]: 'a' != 'b'
    Out[284]: True

    In [285]: 'a' < 'w'
    Out[285]: True

    In [286]: 'A' < 'w'
    Out[286]: True

    In [287]: 'A' < '$'
    Out[287]: False

    In [288]: 'A' < '234$'
    Out[288]: False

    In [289]: 'aaa' < 'AAA'
    Out[289]: False

    In [290]: 'a' < 'A'
    Out[290]: False
    ```

- `ord()`
    - Python uses Unicode for encoding characters used in the string data type
    - The function `ord()` will return the number for any characters
    - examples
        ```
        In [292]: ord('a')
        Out[292]: 97

        In [293]: ord('A')
        Out[293]: 65

        In [294]: ord('B')
        Out[294]: 66

        In [295]: ord('C')
        Out[295]: 67

        In [296]: ord('1')
        Out[296]: 49

        In [297]: ord(' ')
        Out[297]: 32

        In [298]: ord('.')
        Out[298]: 46

        In [299]: '100' < '9'
        Out[299]: True

        In [300]: ord('100')
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[300], line 1
        ----> 1 ord('100')

        TypeError: ord() expected a character, but string of length 3 found

        In [301]: ord('"100"')
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[301], line 1
        ----> 1 ord('"100"')

        TypeError: ord() expected a character, but string of length 5 found

        In [302]: ord('1')
        Out[302]: 49

        In [303]: ord('11')
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[303], line 1
        ----> 1 ord('11')

        TypeError: ord() expected a character, but string of length 2 found

        In [304]: help("ord")

        ```
## Booleans In The Wild

## Assignment