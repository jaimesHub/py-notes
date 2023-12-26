# Variables Basics

## Introduction Variables
- Basic Data Types
- Variables are what we use to actually `store values` and give them a `label` (Are like `labels` for `values`)
- We treat `a variable` as `a jar/a container` that has some values in it. Then `a label` associated with it, like a `name` tag
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

## Variable Naming
- `Convention*` naming: acceptable python names for variables
    - `Valid`: variables123, first_name (Pythonic), player_1 (Pythonic)
    - `Invalid`: 123variable, first name, False, def
    - `Not good`: FirstName, FIRSTNAME, I, O, x
- Pythonic approach, Pythonic name
    - The Python convention of `snake_case` for `variables names`
- Python Keywords
    - >>> help("your_keywords_want_to_know")
- `Meaning names` means you should use names that `make sense`
- If you have a `variable` that will `never change` something called a `constant`
    - PI = 3.14

## Assignment Operators
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

## How Variables Work?
- [Page 32](https://www.canva.com/design/DAErfXIn0Ak/0CgknsGzKJ_TnrcJNWUIdg/view)

## The Print() Function
- The `print()` function prints out any values we pass to it to "standard output". It does not return anything
- >>> print("hello")

## Numbers & Variables In The Wild

## Assignment
- Check `magic_trick_starter.py`