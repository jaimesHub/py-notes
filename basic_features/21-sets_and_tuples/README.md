# Sets And Tuples

## Introducing Tuples
- Immutable, ordered collections
    - `Like` lists, tuples are ordered, indexed collections
    - `Unlike` lists, `tuples are immutable`. They cannot change once created

- Create a Tuple
    > dishes = ("burrito", "taco", "fajita", "quesadilla")
    - parentheses
    - commas

- Empty Tuple
    > empty_tuple_way_1 = ()
    > empty_tuple_way_2 = tuple()

- 1 Item Tuple
    > single_tuple = ("First") # `ERROR`
    > single_tuple = "First", # `VALID`
    > single_tuple = ("First", ) # `VALID`

## Tuple Functionality
- What we can and can't do with tuple
- Actions in Code
    - Example: `> dishes = ("burrito", "taco", "fajita", "quesadilla")`
    - Access: 
        > dishes[2]
        fajita

    - Slice:
        > dishes[1:3]
        ("taco", "fajita")

    - Index:
        > dishes.index("taco")
        1

    - in:
        > "nachos" in dishes
        False
    - for:
        > for dish in dishes:
            print(dish)
        burrito
        taco
        fajita
        quesadilla
    
    - Unpacking:
        > items = ("312", "31th Ave", "New York", "New York")
        > number, street, city, state = item
        > number
        312
        > street
        31th Ave
        > city
        New York
        > state
        New York

## Why Use Tuples?
- they are more efficient than lists
- use them for data that shouldn't change
- some methods return them like dict.items()
- they can be used as `keys` in a `dictionary`

## Sets Introduction
- `Unordered` collections with `no duplicate elements`
- Only `immutable` elements!
- We can...
    - add and delete elements
    - iterate over elements
    - check to see if element is in a set
    - use set operators: union, intersection,...

## Working With Sets
- Creating Sets
    > evens = {2, 4, 6, 8}
- Empty Set
    > empty_set = {} # `ERROR`
    > empty_set = set() # `VALID`
- add(): adds a single value to a set. No duplicates in sets!
    > evens = {2, 4, 6, 8}
    > even.add(12)
    > even
    {2, 4, 6, 8, 12}
- remove(): removes a single value from a set
    > langs = {"Python", "C", "JavaScript"}
    > langs.remove("C")
    > langs
    {"Python", "JavaScript"}
- discard(): like `remove()` but won't throw `error` for `missing` value
    > langs = {"Python", "C", "JavaScript"}
    > langs.discard("C")
    > langs
    {"Python", "JavaScript"}
- clear(): empties out a set
    > langs = {"Python", "C", "JavaScript"}
    > langs.clear()
    > langs
    set()

## Set Operators: Intersection, Union, Difference
- Intersection: 
    - returns new set with members common to left and right
    - left & right
- Union: 
    - returns new set with members form left and right
    - left | right
- Difference: 
    - returns new set with members from `left` `not` in `right`
    - left - right

## When Use Sets?
    - Sets make it very easy/fast to check if a value exists in a collection
    - Sets are an easy way to remove duplicates from a collection
    - heavy lifts