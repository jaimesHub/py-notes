# Strings And Built-ins

## Introducing Functions!
- Functions are `reusable actions` that have a name
- To `execute` a function, we write its name with parentheses opening and closing, sometimes pass some between parentheses
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
    - arguments is a name for the inputs we provide to a function.
    - burger (bun, secret_sauce, lettuce, tomato, bacon, cheese, well_done)
    - burger (lettuce_wrap, ketchup, tomato, swiss_cheese, well_done)
- built-in functions

## The Len Function
- The `len()` function will return the `length` of whatever item we pass to it. 
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

## The Input Function
- The `input()` function will prompts a user to enter some input, converts it into a string and then returns it
- We can use it to gather user input in our programs
- Example: `input.py`

## Type Casting
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

## F-Strings
- `f-strings` are an easy way to `generate strings` that contain `interpolated expressions`.
- Any code between `curly braces {}` will be evaluated and then the result will be turned into a string and inserted into the overall string.
- It treats it as a non string. It will evaluate the contents of the curly braces.
- Examples
    ```
    In [128]: "the price is 4*67.99"
    Out[128]: 'the price is 4*67.99'

    In [129]: f"the price is {4*67.99}"
    Out[129]: 'the price is 271.96'
    ```

## F-String And Type Casting In The Wild

## Assignment
- Check `shopping_cart.py`