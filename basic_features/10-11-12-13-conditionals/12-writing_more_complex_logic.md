# Writing More Complex Logic

## Logical AND
- The `and` operator will evaluate to True only if both the left and right sides evaluate to True
- `'a' == 'a' and 1 < 5`
- Graphic to try and explain how it works
- Python uses `and` keyword
- Examples
```
In [331]: 3 < 4 and 3 != 8
Out[331]: True

In [332]: True and True
Out[332]: True

In [333]: True and False
Out[333]: False

In [334]: False and False
Out[334]: False

In [335]: False and True
Out[335]: False
```

## Using Logical AND in practice
- Check `logical_and.py`

## Logical OR
- The `or` operator will evaluate to True if one of both the left or right sides evaluate to True
- Example
```
'a' == 'b' or 1 < 5>
In [337]: True or False
Out[337]: True

In [338]: False or True
Out[338]: True

In [339]: False or False
Out[339]: False

In [340]: True or True
Out[340]: True
```

## Using Logical OR in Practice
- Check: `logical_or.py`

## Logical NOT
- The `not` operator changes True to False and False to True. It negates expressions.
- Example
```
In [341]: 1 < 5
Out[341]: True

In [342]: not 1 < 5
Out[342]: False

In [343]: 1 < 5 not
  Cell In[343], line 1
    1 < 5 not
             ^
SyntaxError: invalid syntax
```

## Using Logical NOT in practice
- check: `logical_not.py`