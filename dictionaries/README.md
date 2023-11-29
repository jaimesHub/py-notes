# Dictionaries

## Introducing Dictionaries
- How would we store data ?
- Dictionaries allow us to store information in key-value pairs
- `key-value` pairs in `dictionaries` vs `index-value` pairs in `lists`

## Creating Your Own Dictionaries
- empty dict
    ```
        In [1]: {}
        Out[1]: {}

        In [2]: type({})
        Out[2]: dict

        In [3]: dict()
        Out[3]: {}
    ```
- syntax: 
    - order = {"cost": 3.5, "quantity":12}
- Notes: Dictionaries, known as associative arrays in some other languages, `are indexed by keys` rather than a numerical index
    - A dictionary holds key-value pairs
    - Keys can be any immutable type: numbers, strings, booleans,...
        - Example
        ```
            In [8]: {3: "three"}
            Out[8]: {3: 'three'}

            In [9]: {[1,2,3]: "HELLO!"}
            ---------------------------------------------------------------------------
            TypeError                                 Traceback (most recent call last)
            Cell In[9], line 1
            ----> 1 {[1,2,3]: "HELLO!"}

            TypeError: unhashable type: 'list'
        ```
    - Values can be whatever you want!


## Accessing Data In Dictionaries
- retrieve values using `dict[key]`
- Examples:
```
In [11]: nums = [1,2,3,4]

In [12]: nums[0]
Out[12]: 1

In [13]: movie
Out[13]: {'title': 'Amadeus', 'imdb_score': 8.3}

In [14]: movie["title"]
Out[14]: 'Amadeus'

In [15]: movie["t"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[15], line 1
----> 1 movie["t"]

KeyError: 't'

In [16]: movie["Title"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[16], line 1
----> 1 movie["Title"]

KeyError: 'Title'

In [17]: stuff = {True: "LOL", 45: "hi!"}

In [18]: stuff[45]
Out[18]: 'hi!'

In [19]: stuff[2]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[19], line 1
----> 1 stuff[2]

KeyError: 2

In [20]: stuff[True]
Out[20]: 'LOL'

```

## Adding and Updating Data In Dictionaries
- Examples
```
In [22]: movie["title"]
Out[22]: 'Amadeus'

In [23]: movie["title"] = 'HAHAHA'

In [24]: movie["title"]
Out[24]: 'HAHAHA'

In [25]: movie
Out[25]: {'title': 'HAHAHA', 'imdb_score': 8.3}

In [26]: nums
Out[26]: [1, 2, 3, 4]

In [27]: nums[0] = 'HAHA'

In [28]: nums
Out[28]: ['HAHA', 2, 3, 4]

In [29]: movie['imdb_score'] = 10

In [30]: movie
Out[30]: {'title': 'HAHAHA', 'imdb_score': 10}

In [31]: movie['imdb_score'] += 10

In [32]: movie
Out[32]: {'title': 'HAHAHA', 'imdb_score': 20}
```

- Examples
```
In [24]: movie["title"]
Out[24]: 'HAHAHA'

In [25]: movie
Out[25]: {'title': 'HAHAHA', 'imdb_score': 8.3}

In [26]: nums
Out[26]: [1, 2, 3, 4]

In [27]: nums[0] = 'HAHA'

In [28]: nums
Out[28]: ['HAHA', 2, 3, 4]

In [29]: movie['imdb_score'] = 10

In [30]: movie
Out[30]: {'title': 'HAHAHA', 'imdb_score': 10}

In [31]: movie['imdb_score'] += 10

In [32]: movie
Out[32]: {'title': 'HAHAHA', 'imdb_score': 20}

In [33]: movie['rating'] = 'R'

In [34]: movie
Out[34]: {'title': 'HAHAHA', 'imdb_score': 20, 'rating': 'R'}

In [35]: movie['rating']
Out[35]: 'R'

In [36]: movie['is_great'] = True

In [37]: movie
Out[37]: {'title': 'HAHAHA', 'imdb_score': 20, 'rating': 'R', 'is_great': True}

In [38]: movie['my_score'] = 20

In [39]: movie
Out[39]: 
{'title': 'HAHAHA',
 'imdb_score': 20,
 'rating': 'R',
 'is_great': True,
 'my_score': 20}
```

## The get() method and `in` operator
- `farmstand.py`
- the `in` operator only looks at the `keys`
- the `get()` method will look for `a given key` in a `dictionary`. If the key `exists`, it will return the `corresponding value`. Otherwise it returns `None`

## Dictionary pop(), clear() and del
- the `pop()` method accepts a key and will delete the corresponding key-value pair in the dictionary. It returns the deleted value
    - example:
        > dict1 = {"a": 1, "b": 1, "c":3}
        > pop_value = dict1.pop('b')
        > pop_value
        1
- the `popitem()` method deletes the most recently added key-value pair. It returns the item as a tuple
    - example:
        > dict1 = {"a": 1, "b": 1, "c":3}
        > pop_item = dict1.popitem()
        > pop_item
        ('c', 3)
- the `clear()` deletes all items from a dictionary. It returns None.
- we also use the `del statement` to remove items from a dictionary. It's `not` a method!

## Dictionaries Are Mutable Too!
- same as list

## Iterating Dicts: keys(), values() and items()
- `iterating_dicts.py`
- `keys()`
    ```
    In [47]: test_scores.keys()
    Out[47]: dict_keys(['Marsha', 'Baker', 'Rosa', 'Leif', 'Peng', 'Juan', 'Esteban', 'Amir', 'Sakura'])

    In [48]: type(test_scores.keys())
    Out[48]: dict_keys
    ```
- `values()`
    ```
    In [49]: test_scores.values()
    Out[49]: dict_values([78, 69, 92, 97, 61, 73, 84, 91, 99])

    In [50]: type(test_scores.values())
    Out[50]: dict_values
    ```

- `items()`
    ```
    In [51]: test_scores.items()
    Out[51]: dict_items([('Marsha', 78), ('Baker', 69), ('Rosa', 92), ('Leif', 97), ('Peng', 61), ('Juan', 73), ('Esteban', 84), ('Amir', 91), ('Sakura', 99)])

    In [52]: type(test_scores.items())
    Out[52]: dict_items
    ```
## Fancy Dictionary Merging
- The `update` method will update a dictionary using the key-value pairs from a second dictionary, passed as the argument
- Example
    > order = {"cost": 3.5, "quantity":12}
    > order.update({"product": "taco", "date": "01/01/2023"})
    > order
    {"cost": 3.5, "quantity":12, "product": "taco", "date": "01/01/2023"}

- We can use two stars `**` to combine multiple dictionaries into a new resulting dictionary
- Example
    > dict1 = {"a": 1, "b": 2}
    > dict2 = {"c": 3, "d": 4}
    > dict3 = {**dict1, **dict2}
    > dict3
    {"a": 1, "b": 2, "c": 3, "d": 4}

- The dict `union` operator (|) - `Python 3.9`
    - It will return a new dict containing the items from the left and the right dicts.
    - In the case of duplicated keys, the right side `wins`
    - examples
        > dict1 = {"a": 1, "b": 2}
        > dict2 = {"c": 3, "d": 4}
        > dict3 = dict1 | dict2
        > dict3
        {"a": 1, "b": 2, "c": 3, "d": 4}


## Lists and Dicts Combined!
- `dicts_and_lists.py`

## Exercise
- `dictionary_peak.py`