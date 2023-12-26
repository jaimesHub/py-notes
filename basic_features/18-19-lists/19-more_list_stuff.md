# More List Stuff

## Nested Lists
- Example
    ```
        In [55]: stuff = ["hi!", True, [], [1,2,3]]

        In [56]: stuff
        Out[56]: ['hi!', True, [], [1, 2, 3]]

        In [57]: super_nested = [[[[[]]]]]

        In [58]: super_nested
        Out[58]: [[[[[]]]]]

        In [59]: nums = [1,2,3,4,[5,6]]

        In [60]: nums
        Out[60]: [1, 2, 3, 4, [5, 6]]

        In [61]: nums[4]
        Out[61]: [5, 6]
    ```
- Example
    ```
    In [63]: couples = [
    ...:     ["Beyonce", "Jay-Z"],
    ...:     ["Johnny", "June"],
    ...:     ["John", "Yoko"],
    ...:     ["Will", "Jada"]
    ...: ]
    ...: 
    ...: 

    In [64]: couples
    Out[64]: [['Beyonce', 'Jay-Z'], ['Johnny', 'June'], ['John', 'Yoko'], ['Will', 'Jada']]

    In [65]: len(couples)
    Out[65]: 4

    In [66]: couples[1]
    Out[66]: ['Johnny', 'June']

    In [67]: cash = couples[1]

    In [68]: cash[0]
    Out[68]: 'Johnny'

    In [69]: couples[1][0]
    Out[69]: 'Johnny'

    In [70]: couples[1][0][5]
    Out[70]: 'y'

    In [71]: couples[2]
    Out[71]: ['John', 'Yoko']
    ```
- `nested_lists.py`

## List Operators
- Addition
```
In [73]: 1 + 2
Out[73]: 3

In [74]: "aa" + "bb"
Out[74]: 'aabb'

In [75]: [1,2,3] + [3,4]
Out[75]: [1, 2, 3, 3, 4]

In [76]: evens = [2,4,6]

In [77]: odds = [1,3,5]

In [78]: evens + odds
Out[78]: [2, 4, 6, 1, 3, 5]

In [79]: evens
Out[79]: [2, 4, 6]

In [80]: odds
Out[80]: [1, 3, 5]

In [81]: both = evens + odds

In [82]: both
Out[82]: [2, 4, 6, 1, 3, 5]

In [83]: evens + 1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[83], line 1
----> 1 evens + 1

TypeError: can only concatenate list (not "int") to list
```

- Multiplication
```
In [85]: [1,2,3] * 2
Out[85]: [1, 2, 3, 1, 2, 3]

In [86]: "hi" * 6
Out[86]: 'hihihihihihi'

In [87]: "d" * "d"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[87], line 1
----> 1 "d" * "d"

TypeError: can't multiply sequence by non-int of type 'str'

In [88]: evens
Out[88]: [2, 4, 6]

In [89]: evens * 3
Out[89]: [2, 4, 6, 2, 4, 6, 2, 4, 6]

In [90]: evens
Out[90]: [2, 4, 6]

In [91]: 2 * [1,2,3]
Out[91]: [1, 2, 3, 1, 2, 3]

In [92]: "a" in "happy"
Out[92]: True

In [93]: 4 in evens
Out[93]: True

In [94]: 5 in evens
Out[94]: False
```

- `in_demo.py`

## Sort(), Reverse() and Count()
- The `count` method returns the number of times a value occurs in a list. If the value is not in the list, it returns 0
- The `reverse()` method reverses a list `in-place`
- The `sort()` method sorts the list in ascending order and return None.

## Lists Are Mutable
- How List works behind the scence?
- Example
```
In [101]: id?
Signature: id(obj, /)
Docstring:
Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)
Type:      builtin_function_or_method

In [102]: id(34)
Out[102]: 4351316736

In [103]: id(34)
Out[103]: 4351316736

In [104]: id(34)
Out[104]: 4351316736

In [105]: id(34)
Out[105]: 4351316736

In [106]: id(True)
Out[106]: 4350364312

In [107]: id(0)
Out[107]: 4351315648

In [108]: id(1)
Out[108]: 4351315680

In [110]: id([])
Out[110]: 4383553344

In [111]: id([])
Out[111]: 4388496384

In [112]: id([])
Out[112]: 4382170112

In [113]: l = [1,2,3]

In [114]: id(l)
Out[114]: 4382576704

In [115]: id(l)
Out[115]: 4382576704

In [116]: id(l)
Out[116]: 4382576704

In [117]: id([])
Out[117]: 4388608512

In [118]: num = 5

In [119]: age = num

In [120]: age += 1

In [121]: num
Out[121]: 5

In [122]: age
Out[122]: 6

In [123]: nums_1 = [1,2,3]

In [124]: nums_2 = nums_1

In [125]: id(nums_1)
Out[125]: 4388483520

In [126]: id(nums_2)
Out[126]: 4388483520

In [127]: nums_2.append(4)

In [128]: nums_2
Out[128]: [1, 2, 3, 4]

In [129]: nums_1
Out[129]: [1, 2, 3, 4]
```

## Comparing Lists: == vs is
- Use `==` to compare the contents inside of two lists. Do they hold the same values ?
    - They contain the same values
    - Order is matter
- Use `is` to compare the identity of two lists. Are they the same `container` in memory?
    - Check whether 2 lists refer to the same list in memory or not
    - Any changes to one of 2 lists will also appear on the remain one

## Join() and Split()
- `split()` is a string method that will split a string on a given character. It returns a list that holds the split strings
- `join()` is a string method that joins together the elements of an iterable into a string. Whatever string you call it on will be used as a separator

## List Unpacking
- We can `unpack` values from a list into specific variables
- Example
    > users = ["Joe", "Bucky", 42]
    > first, last, age = users
    > first
    "Joe"
    > last
    "Bucky"
    > age
    42
- `*` Unpacking
    > item = [4, "Pizza", "Plain", 16.98]
    > quantity, *others, price = item
    > quantity
    4
    > others
    ["Pizza", "Plain"]
    > price
    16.98

## Copying Lists
- The `copy` method returns a `shallow copy` of a list. Nested objects are not copied
    - We can also copy lists by creating slices of an entire list. It's not the most readable, but it works
    - Example
        ```
        In [131]: list1 = [2,9,['a', 'b'],7]

        In [132]: list1.copy?
        Signature: list1.copy()
        Docstring: Return a shallow copy of the list.
        Type:      builtin_function_or_method

        In [133]: list2 = list1.copy()

        In [134]: list2
        Out[134]: [2, 9, ['a', 'b'], 7]

        In [135]: list1
        Out[135]: [2, 9, ['a', 'b'], 7]

        In [136]: id(list1)
        Out[136]: 4388561856

        In [137]: id(list2)
        Out[137]: 4382213568

        In [138]: list1 == list2
        Out[138]: True

        In [139]: list1 is list2
        Out[139]: False
        ```
- The `deepcopy()` method will make a copy of a list AND any nested objects contained inside that list
    > import copy
    > list1 = [2,9,['a', 'b'],7]
    > list2 = copy.deepcopy(list1)

## Quick Summary
- Shallow copy
    - `independent` object `(1)`
    - because we only created a `shallow` copy of the original list, copied object still contains `references` to the `original` child objects stored in original object. `(2)`
- Deep copy
    - same `(1)`
    - difference with `(2)`

## Exercise
- `todos.py`
- https://plum-poppy-0ea.notion.site/Todo-List-Exercise-87d17f24feb74e799086acbb9c875719
- [copy vs deep copy](https://docs.python.org/3/library/copy.html)
- [shallowcopy vs deepcopy](https://realpython.com/copying-python-objects/)