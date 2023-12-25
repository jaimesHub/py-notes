# Working With Errors
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Exception-hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

## Common Error Types
- [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)
- [NameError](https://docs.python.org/3/library/exceptions.html#NameError)
- [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
- [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)

## Raising Exceptions
- `raise.py`
- `raise`
    - We can raise our own exceptions (force them happen) whenever we want, using the `raise` keyword
        - `raise ValueError`
    - You can also provide a specific message when raising an exception
        - `raise ValueError("invalid character")`
    - Example
    ```
    In [1]: raise Exception
    ---------------------------------------------------------------------------
    Exception                                 Traceback (most recent call last)
    Cell In[1], line 1
    ----> 1 raise Exception

    Exception: 

    In [2]: raise IndexError
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    Cell In[2], line 1
    ----> 1 raise IndexError

    IndexError: 

    In [3]: raise ValueError("invalid character")
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    Cell In[3], line 1
    ----> 1 raise ValueError("invalid character")

    ValueError: invalid character

    In [4]: int('f')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    Cell In[4], line 1
    ----> 1 int('f')

    ValueError: invalid literal for int() with base 10: 'f'
    ```



## When To Raise?
- handling something wrong/not sure
- `raise.py`

## Try And Except
- `try.py`
- `try/except`
    - We can use the `try` and `except` keywords to `handle exceptions`.
    - If an exception is raised in the try block, the except block will run
    - Syntax:
        ```
            try:
                <code that could generate error>
            except:
                <code that runs if error raised>
        ```
    - Usually it's `better` to except a `specific` exception and handle it, rather than handling any possible exception that could occur.
        ```
            try:
                num = int(input("Please enter a number: ))
            except ValueError:
                print("Oh no, that isn't a number!")
        ```
- `multiple excepts`
    ```
        try:
            num = int(input("Enter an integer: "))
            print(10/num)
        except ValueError:
            print("That's not an int!")
        except ZeroDivisionError:
            print("Can't divide by zero!")
    ```

## LBYL and EAFP approaches
- You can use both of them

### EAFP
- Just do it, if it doesn't work we will say sorry later (raise exceptions)
- `Easier to Ask for Forgiveness than Permission`
- "Assume things exist or will work, and catch exceptions if you're wrong"
- Coding style characterized by lots of try/except blocks

### LBYL
- Check any cases before doing implementation
- `Look Before You Leap`
- Coding style where you explicitly test for pre-conditions before making calls or `leaping`.
Characterized by lots of if statements.