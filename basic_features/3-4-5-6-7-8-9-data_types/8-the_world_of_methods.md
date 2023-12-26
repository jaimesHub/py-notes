# The World Of Mthods

## Introducting Methods: Upper and Lower
- `Methods` are `functions` that `live` on `objects`
- Pattern: `thing.method()`
- Methods automatically have access to the object they are called on
- String Methods:
    ```
    In [134]: "purpleface".upper
    Out[134]: <function str.upper()>

    In [135]: "purpleface".upper()
    Out[135]: 'PURPLEFACE'

    In [136]: "HELLOWORLD".lower()
    Out[136]: 'helloworld'

    In [137]: first_name = "JacKsoN"

    In [138]: first_name.lower()
    Out[138]: 'jackson'

    In [139]: first_name.lower() # make a copy of string
    Out[139]: 'jackson'

    In [140]: first_name
    Out[140]: 'JacKsoN'

    In [141]: first_name = first_name.lower()

    In [142]: first_name
    Out[142]: 'jackson'

    In [143]: first_name.upper()
    Out[143]: 'JACKSON'

    In [144]: first_name.capitalize()
    Out[144]: 'Jackson'

    In [145]: "miCHELLE".capitalize()
    Out[145]: 'Michelle'
    ```

## Navigating The Docs
- Docs: https://docs.python.org/3/
- Categories:
    - `Tutorial`: there's `installation` instructions
    - `Library Reference`: this is the `Encyclopedia` of Python. Different types, all of the methods that they support,...
    - `Language Reference`: it shows a bit about the `syntax` itself of Python, the mechanics of this language, precedence, order,...

## Help() & ipython
- Examples
    ```
    In [147]: help("str")


    In [148]: first_name
    Out[148]: 'jackson'

    In [149]: first_name
    Out[149]: 'jackson'

    In [150]: first_name.capitalize()
    Out[150]: 'Jackson'

    In [151]: first_name.capitalize?
    Signature: first_name.capitalize()
    Docstring:
    Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower
    case.
    Type:      builtin_function_or_method

    In [152]: first_name.strip?
    Signature: first_name.strip(chars=None, /)
    Docstring:
    Return a copy of the string with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
    Type:      builtin_function_or_method

    In [153]: first_name = 99

    In [154]: first_name.upper()
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    Cell In[154], line 1
    ----> 1 first_name.upper()

    AttributeError: 'int' object has no attribute 'upper'

    In [155]: "hello".upper?
    Object `upper` not found.

    In [156]: "hello".upper()?
    Cell In[156], line 1
        "hello".upper()?
                    ^
    SyntaxError: invalid syntax
    ```

## Reading Function Signatures + Strip Methods
- Reading Docs: Reading a `method` or `function`
    - There's a function signature that explains to us using a particular syntax
    - How the function works
    - What it's expecting us to provide to it
- Signatures of a function/method
    - str.upper(`no arguments`)
- str.strip([chars]): removes leading/trailing whitespace characters
    - str.strip(`[chars]`), chars is optional, `[]` means you don't have to provide that
    - the signature `paint([color])` tells us that the color argument is `optional`. So we can call it as `paint()` OR we can provide an argument like `paint("red")` BUT it is not expecting `multiple arguments`.

## Replace
- str.replace(`old`, `new`, [count]), old and new are required, it replaces characters/substrings within a string, count is limitation of the number of occurrences that are replaced by default
- Examples
    ```
    In [175]: races = "3kilometers 5kilometers 10kilometers 41kilometers"

    In [176]: races
    Out[176]: '3kilometers 5kilometers 10kilometers 41kilometers'

    In [177]: races.replace()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[177], line 1
    ----> 1 races.replace()

    TypeError: replace expected at least 2 arguments, got 0

    In [178]: races.replace("kilometers", "km")
    Out[178]: '3km 5km 10km 41km'

    In [179]: races
    Out[179]: '3kilometers 5kilometers 10kilometers 41kilometers'

    In [180]: 

    In [180]: prices = '$1.99 $9.25 $7.50'

    In [181]: prices
    Out[181]: '$1.99 $9.25 $7.50'

    In [182]: prices.replace("$", "")
    Out[182]: '1.99 9.25 7.50'

    In [183]: prices.replace("$", "", 2)
    Out[183]: '1.99 9.25 $7.50'

    In [184]: prices.replace("$", "", 1)
    Out[184]: '1.99 $9.25 $7.50'

    In [185]: races.replace("kilometers", "km", 1)
    Out[185]: '3km 5kilometers 10kilometers 41kilometers'
    ```

## Other String Methods
- Find
    ```
    In [187]: prices
    Out[187]: '$1.99 $9.25 $7.50'

    In [188]: prices.find('$')
    Out[188]: 0

    In [189]: prices.find('9')
    Out[189]: 3

    In [190]: prices.find('$', 1)
    Out[190]: 6

    In [191]: prices.find('$', 7)
    Out[191]: 12

    In [192]: prices.find('$', 7, 9)
    Out[192]: -1

    In [193]: prices.find('.', 7, 9)
    Out[193]: 8

    In [194]: prices.find('2', 7, 9)
    Out[194]: -1

    In [195]: prices.find('9.99')
    Out[195]: -1

    In [196]: prices.find('9.25')
    Out[196]: 7
    ```

- Count
    ```
    In [198]: prices
    Out[198]: '$1.99 $9.25 $7.50'

    In [199]: prices.count('$')
    Out[199]: 3

    In [200]: prices.count('9')
    Out[200]: 3

    In [201]: prices.count('9.')
    Out[201]: 1

    In [202]: prices.count('.')
    Out[202]: 3
    ```

## Method Chaining
    ```
    In [204]: email = 'TODD@gmail.com     '

    In [205]: email.strip()
    Out[205]: 'TODD@gmail.com'

    In [206]: stripped = email.strip()

    In [207]: stripped
    Out[207]: 'TODD@gmail.com'

    In [208]: stripped.lower()
    Out[208]: 'todd@gmail.com'

    In [209]: clean_email = stripped.lower()

    In [210]: clean_email
    Out[210]: 'todd@gmail.com'

    In [211]: email = 'TODD@gmail.com     '

    In [212]: email
    Out[212]: 'TODD@gmail.com     '

    In [213]: email.strip().lower()
    Out[213]: 'todd@gmail.com'

    In [214]: email.count('D')
    Out[214]: 2

    In [215]: email.count('D').lower()
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    Cell In[215], line 1
    ----> 1 email.count('D').lower()

    AttributeError: 'int' object has no attribute 'lower'
    ```

## String Methods In The Wild

## Assignment
- check `press_release.py`

# References
- [Difference Between Methods and Functions in Python](https://www.shiksha.com/online-courses/articles/difference-between-methods-and-functions-in-python/)