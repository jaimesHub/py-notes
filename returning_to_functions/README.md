# Returning To Functions

## Introducing *args
- We can use the `wildcard` or `*` notation to write functions that accept `any number of arguments`

## Using *args
- Example
```
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)
```
- `*args` -> gathers all remaining arguments into a tuple
    - Pass as many arguments as we want! 5 args in this case:
    > average`(1,2,3,4,5)`
    3.0
    - 2 arguments in this example:
    > average`(10,1)`
    5.5
- `args` is common, but `NOT` required. You can name any word as long as it makes sense
```
def average(*nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)
```

## Introducing **kwargs
- We can use the `**` notation to write functions that accept `any number of keyword arguments`
- Example
```
def print_ages(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} is {v} years old")
```
- `**kwargs`: gathers all keyword arguments into a dictionary
    - print_ages(max=67, sue=59, kim=14)
- name (`**kwargs`) is just a parameter. You can name this whatever you want
```
def print_ages(**ages):
    for k,v in ages.items():
        print(f"{k} is {v} years old")
print_ages(max=67, sue=59, kim=14)
```

## Parameter List Ordering
- When defining functions, the order of parameters matters!
- Order maters (`parameters`, `*args`, `default parameters`, `**kwargs`)

## A Common Gotcha: Mutable Default Args
- With mutable default arguments

## Unpacking Args
- Turning sequences into separate args

## Assignment