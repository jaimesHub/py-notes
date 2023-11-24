# One Week Python

## Section 1: Welcome & Introduction
- This course is 
    - A fast , effective pathway to learn Python
    - Full of exercises, challenges, quizzes
    - Avarage video is 4mins
    - An ideal on ramp to DS, ML, Web
- This course is not for
    - Duration 60h
    - Advanced concepts, experts
    - Web/DS/ML
- Focus on `Fundamental` things

## Section 2: Installation & Setup
- Installation
    - Download: https://www.python.org/downloads/
- Running Python: 2 ways we can run Python code
    - Interactively: terminal
        - python3 --version: checking version
        - python3: open interactive mode, exit()/Ctrl + D
        - IPython: python3 -m pip install ipython
    - From A File:
        - Writing python code in a file (`game.py`)
        - Execute it: `python game.py`
- Setup VSCode
    - Extensions: Python
    - ./Section-2/first.py
- The "No-Installation" Option:
    - REPL.it: https://replit.com/

## Section 3: Python Numbers
### Intro to Data Types
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
- Basic data types: Strings, Integers, Booleans, Floats
### Integers and Floats
- There are 2 important numeric types: `Integers` and `floats`
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
        - How: `type(variable)` tell us the type of that variable. e.g. type(6) -> int, type(5.6) -> float
        - it takes more memory to do math with `floats` versus `ints`
        - integers `are` actually unbounded. e.g. 35734890527432857431573445834290213462378493754
        - floats are `not` unbounded. e.g. 2.333333333333333333333333 -> 2.3333333333333335
        -> there is `a level of precision` that we run up agains with `floats`
### Numberic Notations
- ints: 
    - 31000000 or 31_000_000 `not` 31,000,000
    - 09 -> error
- floats: 
    - 1000.5 or 1_000.5 `not` 1,000.55
    - 1.234e12 `not` 1.234 e12
    - 6.7e-10, 6.7e-3
### Basic Operators
- Concepts
- Example
    - Addition: 5 + 2, 5.4 + 2
    - Subtraction: 3 - 1, 4 - 1.0
    - Asterisk: 45 * 12
    - Division: 5 / 2, 10 / 2.6
- Order of Operations
    - Parentheses: `()`
    - Multiplication and Division: `*, /. //`
    - Addition anf Subtraction: `+, -`
### Lesser Known Operators
- Integer Division: `//`, it rounds down the result
- Exponentiation: `**`
- Modulo: `%`, remainders of ... , check even or odd numbers
### Python Comments
- Python will ignore any lines starting with the `#` symbol
- e.g. `# this never runs`

## Section 4: Variables Basics
### How Variables Work?

### Introduction Variables
- Basic Data Types
- Variables are what we use to actually `store values` and give them a `label` (Are like `labels` for `values`)
- We treat `a variable` as a jar/a container that has some values in it. Then `a label` associated with it, like a `name` tag
    - Refer back to it later
    - Use that value to do ...stuff
    - Change it later on
- For example: 
    - A jar (product) has `label` is `age`, which contains `value` as `price` is 48.
    - Refer back to it later: means we will back to buy it after walk around the supermarket
    - Use that value to do ...stuff: means we will use its `price` (value) to compare other product
    - Change it later on: means we can use voucher to get discount for this product
- Variables: How we actually make them?
    - score     =          170
    - ^         ^           ^
    - variable  assignment Value
    -> python created `memory location` for `score` variable (as a QR code)
    - Example 1: Using Ipython
    ```
        In [6]: age = 18

        In [7]: age
        Out[7]: 18

        In [8]: age + 1
        Out[8]: 19

        In [9]: age
        Out[9]: 18

        In [10]: age = age + 1

        In [11]: age
        Out[11]: 19
    ```
    - Example 2: Using Ipython
    ```
        In [12]: score = 500

        In [13]: score
        Out[13]: 500

        In [14]: Score
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        Cell In[14], line 1
        ----> 1 Score

        NameError: name 'Score' is not defined
    ```
    - Exmaple 3: Using Ipython
    ```
        In [16]: score
        Out[16]: 500

        In [17]: score * 3
        Out[17]: 1500

        In [18]: score
        Out[18]: 500

        In [19]: score = score * 3

        In [20]: score
        Out[20]: 1500

        In [21]: score = 0

        In [22]: score
        Out[22]: 0
    ```
    - Example 4: Using Ipython
    ```
        In [23]: age
        Out[23]: 19

        In [24]: score
        Out[24]: 0

        In [25]: score = 999

        In [26]: age * score
        Out[26]: 18981
    ```

### Variable Naming
- Convention naming: acceptable python names for variables
    - `Valid`: variables123, first_name (Pythonic), player_1 (Pythonic)
    - `Invalid`: 123variable, first name, False, def
    - `Not good`: FirstName, FIRSTNAME, I, O, x
- Pythonic approach, Pythonic name
    - The Python convention of snake_case for variables names
- Python Keywords
    - >>> help("keywords")
- Meaning names means you should use names that make sense
- If you have a variable that will never change something called a `constant`
    - PI = 3.14

### Assignment Operators
- A new group of operators that all have to do with variables and reassigning a value or updating value
- `+=` operator
    ```
        In [1]: prize_money = 500

        In [2]: prize_money = prize_money + 50

        In [3]: prize_money
        Out[3]: 550

        In [4]: prize_money += 50

        In [5]: prize_money
        Out[5]: 600
    ```
- `-=` operator
    ```
        In [5]: prize_money
        Out[5]: 600

        In [6]: prize_money -= 100

        In [7]: prize_money
        Out[7]: 500
    ```
- `*=` operator
    ```
        In [7]: prize_money
        Out[7]: 500

        In [8]: prize_money *= 10

        In [9]: prize_money
        Out[9]: 5000
    ```
- `/=` operator
    ```
        In [9]: prize_money
        Out[9]: 5000

        In [10]: prize_money /= 100

        In [11]: prize_money
        Out[11]: 50.0
    ```
- `//=` operator
- `**=` operator
- `%=` operator

### Numbers & Variables In The Wild

### The Print() Function
- The `print()` function prints out any values we pass to it to "standard output". It does not return anything
- >>> print("hello")

## Section 5: String Basics
### How Variables Work?

### Introducing Strings
- Basic Data Types
- "STRINGS OF CHARACTERS"
- Strings are a textual datatype and must be wrapped in quotes
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

### String Variables
- Change type
```
age = 85
age = "eighty five"
```

### String Operators
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
- Multiplication: We can also multiply a string by a number, which will repeat that string
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
### String Indexing
- Strings Are Ordered
- Strings Are Indexed
- Indexes: it starts counting it zero
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
- We can use a `negative` index starting from the end of the string (the last character)
- Examples
    ```
    In [50]: first_name[-1]
    Out[50]: 'y'

    In [51]: first_name
    Out[51]: 'Tammy'
    ```

### The Special Value None
- `None` is a special value in Python that denotes the `lack of value`. It is `not` the same as `zero` or an `empty string` (`those are still values`) ~ `NULL` value in JS
- It is emptiness, it means nothing
- It is very different from zero or an empty string, those are still value

## Section 6: A Little More On Strings
- String `slices`: msg[start:stop]
- Examples
    ```
    In [62]: animal = "catdog"

    In [63]: animal
    Out[63]: 'catdog'

    In [64]: animal[2:4]
    Out[64]: 'td'

    In [65]: animal[3:5]
    Out[65]: 'do'

    In [66]: animal[3:6]
    Out[66]: 'dog'

    In [67]: animal[3:99]
    Out[67]: 'dog'

    In [68]: animal
    Out[68]: 'catdog'

    In [69]: animal[3:]
    Out[69]: 'dog'

    In [70]: animal[0:4]
    Out[70]: 'catd'

    In [71]: animal[0:3]
    Out[71]: 'cat'

    In [72]: animal[:3]
    Out[72]: 'cat'
    ```
- Examples
    ```
    In [74]: pn1 = "(310) 448 8712"

    In [75]: pn2 = "(212) 696 9912"

    In [76]: pn1[1:4]
    Out[76]: '310'

    In [77]: pn2[1:4]
    Out[77]: '212'

    In [78]: sns = "#2523598274"

    In [79]: sns[1:]
    Out[79]: '2523598274'
    ```
- Slices with a Step: `msg[start: stop: step]`
- Examples
    ```
    In [81]: msg = 'ha!ha!ha!ha!'

    In [82]: msg[0:10]
    Out[82]: 'ha!ha!ha!h'

    In [83]: msg[0:10:3]
    Out[83]: 'hhhh'

    In [84]: msg[0:10:2]
    Out[84]: 'h!ah!'

    In [85]: msg[0:10:5]
    Out[85]: 'h!'
    ```
- Revisiting `Print()`
- Escape Characters
    - Newline: `\n` -> a new line character that will be displayed when we `print` this string
    ```
        In [87]: "hello \n world"
        Out[87]: 'hello \n world'

        In [88]: print("hello \n world")
        hello 
        world

        In [89]: phrase = "hello\nworld"

        In [90]: print(phrase)
        hello
        world
    ```
    - Tab: `\t`
    ```
    In [91]: print("hello\tworld")
    hello	world
    ```
    - Double: `\"`
    ```
        In [92]: "she said \"lol\""
        Out[92]: 'she said "lol"'

        In [93]: 'she said "lol"'
        Out[93]: 'she said "lol"'
    ```
    - Single Quote: `\'`
    - Backslash: `\\`
    ```
    In [94]: print("\")
    Cell In[94], line 1
        print("\")
            ^
    SyntaxError: unterminated string literal (detected at line 1)

    In [95]: print("\\")
    \
    ```
- Triple Quoted Strings
    ```
    In [97]: """hello"""
    Out[97]: 'hello'

    In [98]: '''
        ...: hello
        ...: world
        ...:     python is a new language
        ...:     it's greate to learn it now
        ...:     "python" is a snake!!!!
        ...: '''
    Out[98]: '\nhello\nworld\n    python is a new language\n    it\'s greate to learn it now\n    "python" is a snake!!!!\n'

    In [99]: print('''
        ...: hello
        ...: world
        ...:     python is a new language
        ...:     it's greate to learn it now
        ...:     "python" is a snake!!!!
        ...: ''')

    hello
    world
        python is a new language
        it's greate to learn it now
        "python" is a snake!!!!


    In [100]: address = '''
        ...: Chicken Little
        ...: 123 Chicken wing lane
        ...: Denver Colorado 21736
        ...: '''

    In [101]: address
    Out[101]: '\nChicken Little\n123 Chicken wing lane\nDenver Colorado 21736\n'

    In [102]: print(address)

    Chicken Little
    123 Chicken wing lane
    Denver Colorado 21736
    ```

## Section 7: Strings & Built-Ins

### Introducing Functions!
- Functions are reusable actions that have a name
- To execute a function, we write its name with parentheses opening and closing, sometimes pass some between parentheses
- inputs      --- executing --- output
  avg(20, 25) ----------------> 22.5
  avg(3,2,5,6)----------------> 4
  get_weather(10003)----------> "23 f"
  login('user', 'password') --> True
- more examples
    ```
    In [104]: help("int")

    In [106]: help(str)


    In [107]: help("string")


    In [108]: type("hello")
    Out[108]: str

    In [109]: print("hello world")
    hello world
    ```
- Arguments (Fancy word for inputs)
    - Arguments is a name for the inputs we provide to a function.
    - burger (bun, secret_sauce, lettuce, tomato, bacon, cheese, well_done)
    - burger (lettuce_wrap, ketchup, tomato, swiss_cheese, well_done)
- built-in functions

### The Len Function
- The len() function will return the length of whatever item we pass to it. 
- Examples
    ```
    In [111]: len
    Out[111]: <function len(obj, /)>

    In [112]: len()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[112], line 1
    ----> 1 len()

    TypeError: len() takes exactly one argument (0 given)

    In [113]: len("hello")
    Out[113]: 5

    In [114]: len(1234)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[114], line 1
    ----> 1 len(1234)

    TypeError: object of type 'int' has no len()

    In [115]: help(len)
    ```

### The Input Function
- The `input()` function will prompts a user to enter some input, converts it into a stringm and then returns it
- We can use it to gather user input in our programs
- Example: `input.py`
### Type Casting
- The `type()` function accepts an input object and will return the type of that object
- Examples
    ```
    In [117]: age = "19"

    In [118]: age
    Out[118]: '19'

    In [119]: int(age)
    Out[119]: 19

    In [120]: type(int(age))
    Out[120]: int

    In [121]: int(age) * 365
    Out[121]: 6935

    In [122]: float(age)
    Out[122]: 19.0

    In [123]: str(276)
    Out[123]: '276'

    In [124]: float(12)
    Out[124]: 12.0

    In [125]: int(1.234)
    Out[125]: 1

    In [126]: int(1.9999)
    Out[126]: 1
    ```
### F-Strings
- `f-strings` are an easy way to generate strings that contain interpolated expressions.
- Any code between `curly braces {}` will be evaluated and then the result will be turned into a string and inserted into the overall string.
- It treats it as a non string. It will evaluate the contents of the curly braces.
- Examples
    ```
    In [128]: "the price is 4*67.99"
    Out[128]: 'the price is 4*67.99'

    In [129]: f"the price is {4*67.99}"
    Out[129]: 'the price is 271.96'
    ```

### F-String And Type Casting In The Wild

## Section 8: The World of Methods
### Introducting Methods: Upper and Lower
- Methods are functions that `live` on objects
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

### Navigating The Docs
- Docs: https://docs.python.org/3/
- Categories:
    - Tutorial: there's installation instructions
    - `Library Reference`: this is the `Encyclopedia` of Python. Different types, all of the methods that they support,...
    - Language Reference: it shows a bit about the syntax itself of Python, the mechanics of this language, precedence, order,...

### Help() & ipython
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

### Reading Function Signatures + Strip Methods
- Reading Docs: Reading a `method` or `function`
    - There's a function signature that explains to us using a particular syntax
    - How the function works
    - What it's expecting us to provide to it
- Signatures of a function/method
    - str.upper(`no arguments`)
- str.strip([chars]): removes leading/trailing whitespace characters
    - str.strip(`[chars]`), chars is optional, `[]` means you don't have to provide that
    - the signature `paint([color])` tells us that the color argument is `optional`. So we can call it as `paint()` OR we can provide an argument like `paint("red")` BUT it is not expecting `multiple arguments`.

### Replace
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

### Other String Methods
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

### Method Chaining
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
### String Methods In The Wild

## Section 9: Booleans

### Introducing Booleans
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
    
### Comparison Operators
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
### Equality Operators
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

### Comparing Across Types
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

### Truthiness & Falseyness
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

### The "in" Operator
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

### Comparing Strings
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
### Booleans In The Wild


