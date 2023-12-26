# The basics

## Creating Lists
- List is the first data structure we learn
- A data structure is a container that can store multiple values at once
- Lists are `ordered collections` of data
- They can hold any of the data types we've seen
- Syntax:
    - Creating List
        - tasks = ["Trash", "Dishes", "Laundry", "Dinner"]
        - tasks = []
        - type(tasks) -> list
        - stuff = [5, 6, True, 'hi', [1,2]]
        - empty_list = list()
        - list("hello") -> ['h', 'e', ..., 'o']
        - list(range(3, 10)) -> [3, 4, 5, ..., 9]

## Accessing Data In Lists
- list_name[index]
- We can retrieve individual elements from a list by passing an index number inside of square brackets.
- Like strings, indices `start` at `0`
- Example
    ```
        In [4]: waitlist = ['tom', "james", "hi"]

        In [5]: waitlist[0]
        Out[5]: 'tom'

        In [6]: 'hello'[0]
        Out[6]: 'h'

        In [7]: waitlist[2]
        Out[7]: 'hi'

        In [8]: waitlist[-1]
        Out[8]: 'hi'

        In [9]: waitlist[-2]
        Out[9]: 'james'

        In [10]: waitlist[1]
        Out[10]: 'james'
    ```

## Updating List Elements
- Update a specific element using its index
- Example
    ```
        In [12]: waitlist
        Out[12]: ['tom', 'james', 'hi']

        In [13]: waitlist[1]
        Out[13]: 'james'

        In [14]: waitlist[1] = 'ammmmm'

        In [15]: waitlist
        Out[15]: ['tom', 'ammmmm', 'hi']

        In [16]: waitlist[0] = 325170348

        In [17]: waitlist
        Out[17]: [325170348, 'ammmmm', 'hi']

        In [19]: waitlist[3]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        Cell In[19], line 1
        ----> 1 waitlist[3]

        IndexError: list index out of range

        In [20]: "hello"[45]
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        Cell In[20], line 1
        ----> 1 "hello"[45]

        IndexError: string index out of range

        In [21]: waitlist[3] = "juan"
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        Cell In[21], line 1
        ----> 1 waitlist[3] = "juan"

        IndexError: list assignment index out of range

        In [22]: waitlist
        Out[22]: [325170348, 'ammmmm', 'hi']
    ```

## append() and extend()
- append(): adds a single value `to the end` of a list
- extend(): accepts an iterable and appends each item from that iterable to the end of the list
- example
    ```
        In [28]: waitlist
        Out[28]: ['jack', 'ammmmm', 'hi']

        In [29]: waitlist.append('abc')

        In [30]: waitlist
        Out[30]: ['jack', 'ammmmm', 'hi', 'abc']

        In [31]: waitlist.append('colt')

        In [32]: waitlist
        Out[32]: ['jack', 'ammmmm', 'hi', 'abc', 'colt']

        In [34]: people = ["charlie", "drew", "emi"]

        In [35]: waitlist.extend(people)

        In [36]: waitlist
        Out[36]: ['jack', 'ammmmm', 'hi', 'abc', 'colt', 'charlie', 'drew', 'emi']
    ```

## insert()
- insert(index, element)
    - `index`: before which to insert the element
    - `element`: element to be inserted into the list
- example
    > nums = [7, 3, 9]
    > nums.insert(1, "hi")
    > nums
    [7, 'hi', 3, 9]

## List Slices
- list[start:stop:end]
- example:
    > stuff = ['c', 6, 'a', 9, 't', 6]
    > stuff[0:2]
    ['c', 6]
    > stuff[0:5:2]
    ['c', 'a', 't']
    > stuff[2:]
    ['a', 9, 't', 6]
    > stuff[:4]
    ['c', 6, 'a', 9]
    > stuff[::2]
    ['c', 'a', 't']
    > stuff[1:3] = [1,2]
    ['c', 1, 2, 9, 't', 6]

- example:
    > nums = [4, 5, 6, 7]
    > nums[1:3]
    [5, 6]
    > nums[1:3] = ['a', 'b', 'c', 'd']
    > nums
    [4, 'a', 'b', 'c', 'd', 7]


## Deletion Methods: pop(), popitems(), remove()
- the `clear()` method removes all items from a list
- the `remove(x)` method will remove the FIRST element in the list that has a value of x
- the `pop()` method removes AND returns the `last` element from a list
    - `pop(index)` also accepts `a specific index`. It will remove the item at that index in the list AND return it
- the `del` statement (it's not a method) can be used to delete an item from a specific index in a list
    - example
        ```
            In [43]: waitlist
            Out[43]: ['jack', 'ammmmm', 'hi', 'abc', 'colt', 'charlie', 'drew', 'emi']

            In [44]: del waitlist[1]

            In [45]: waitlist
            Out[45]: ['jack', 'hi', 'abc', 'colt', 'charlie', 'drew', 'emi']

            In [46]: nums = [2, 6, 8, 2, 4]

            In [47]: nums[2:]
            Out[47]: [8, 2, 4]

            In [48]: del nums[2:]

            In [49]: nums
            Out[49]: [2, 6]

            In [50]: nums = [1,2,3,4,5,6,7,8,9]

            In [51]: nums[::2]
            Out[51]: [1, 3, 5, 7, 9]

            In [52]: del nums[::2]

            In [53]: nums
            Out[53]: [2, 4, 6, 8]
        ```
## Iterating Over Lists
- `iterating_lists.py`

## Lists + Loops Patterns
- `list_loop_patterns.py`

## Exercise
- `grand_prix.py`