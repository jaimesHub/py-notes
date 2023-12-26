# Conditionals Basics

## Introducing Conditionals
- Let's do a little hypothetical: You and a bartender in a bar
- Decisions: Are you over 21?
    - Yes: `Come on in!`
    - No: `Go home kid.`
- Checking: `bartender.py`

## The If Keyword
- if Statement
    - `if condition:`
    - `Indent-4-spaces`: <code here>
- examples:
    ```
        if age >= 21:
            print("Come on in!")
    ```

## The ElIf Keyword
- It means: `If not the first thing, maybe try this instead?`
- Else If Statement
    ```
        if test:
            # code if True
        elif test_2:
            # code if True
    ```
- Example: `ski.py`
    ```
        if color == "green":
            print("Beginner Ski Run")
        elif color == "blue":
            print("Intermediate Ski Run")
        elif color == "black":
            print("Expert Ski Run")
    ```
- `elif` statement only run if the original `if` was False

## The Else Keyword
- If none of the above were True, do this...
- Example: `bartender.py`
- Example:
    ```
        if age < 10:
            print("Your child ticket is $10")
        elif age > 65:
            print("Your senior ticket is $12")
        else:
            print("Your adult ticket is $14")
    ```
- Example: `ski.py`

## Name Length `Codealong`
- How do we make decisions with code and have `different outcomes` ??
- Checking `name_length.py
`
## Generating Random Numbers With Randint()
- Example:
```
In [306]: randint(2, 5)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[306], line 1
----> 1 randint(2, 5)

NameError: name 'randint' is not defined

In [307]: random.randint(2, 5)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[307], line 1
----> 1 random.randint(2, 5)

NameError: name 'random' is not defined

In [308]: 

In [308]: import random

In [309]: random.randint(2,4)
Out[309]: 3

In [310]: random.randint(2,4)
Out[310]: 4

In [311]: random.randint(2,4)
Out[311]: 2

In [312]: random.randint(2,4)
Out[312]: 4
```

- Example:
```
In [314]: from random import randint

In [315]: randint(2, 10)
Out[315]: 2

In [316]: randint(2, 10)
Out[316]: 7

In [317]: randint(2, 10)
Out[317]: 3

In [318]: randint(2, 10)
Out[318]: 4

In [319]: randint(2, 10)
Out[319]: 3

In [320]: randint(2, 10)
Out[320]: 4
```

- Example:
```
In [322]: import random

In [323]: random.randint(1, 10)
Out[323]: 3

In [324]: random.randint(1, 10)
Out[324]: 3

In [325]: random.randint(1, 10)
Out[325]: 3

In [326]: random.randint(1, 10)
Out[326]: 8

In [327]: random.randint(1, 10)
Out[327]: 1

In [328]: random.randint(1, 10)
Out[328]: 8

In [329]: random.randint(1, 10)
Out[329]: 5
```

- Example: `cointoss.py`

## Assignment
- [Reference](https://plum-poppy-0ea.notion.site/Conditionals-Tweet-Checker-Exercise-0ca1730428424073a7eb868e6135db6c)
- `twitter_checker.py`