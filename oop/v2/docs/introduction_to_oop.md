# Introduction to OOP

## What
- Object oriented programming (OOP) is a `method` of programming that attempts to `model` some `process` or `things` which exist in the (real) world as a `class` or `object`.
- `class` - a `blueprint` for objects. Classes can contain `methods` (functions) and `attributes` (similar to keys in a `dict`).
- `instance` - objects that are `constructed` from `a class blueprint` that contain their class's `methods` and `properties`.
- Example
```
In [1]: help(int)
In [2]: help(list)
In [3]: nums = [1,2,3] # create an instance of list
In [4]: type(nums)
Out[4]: list
```
- Class names should follow the `UpperCaseCamelCase` convention

## Why
- The goal is to `encapsulate` your code into `logical`, `hierarchical groupings` using classes so that you can reason about your code at a higher level.
- Easy for human
- Breaking down a huge problem into small parts

## Example
- Modeling a game of `poker`
    - Entities: Game, Player, Card, Deck, Hand, Chip, Bet
    - Each entity could be its own class in our program

- example without OOP

- example with OOP
    - Pseudocode
    - Deck {class}
        - _cards -> {private list attribute}
        - _max_cards -> {private int attribute}
        - shuffle -> {public method}
        - deal_card -> {public method}
        - deal_hand -> {public method}
        - count -> {public method}
- Python does `not` actually support `true` private/public variables or attributes/methods. It is just a convention.

## Encapsulation
- `Encapsulation` - the grouping of public and private `attributes` and `methods` into a programmatic class, `making` abstraction possible
- Example
    - Designing the `Deck` class, I make cards a `private attribute` (a list)
    - I decide that the `length` of the cards should be `accessed` via a `public method` called `count()` -- i.e. Deck.count()

## Abstraction
- `Abstraction` - exposing only "`relevant`" data in a class `interface`, `hiding private attributes` and `methods` (aka the "`inner workings`") from users
- Example
    - As a user of the `Deck` class, I `never` call `len(Deck.cards)`, only `Deck.count()` because `Deck.cards` is "`abstracted away`" for me.

## Creating a Class
- Example: `user.py`
- Classes in Python can have a special `__init__()` method, which gets called `every time` you `create an instance of the class` (instantiate)
    - It means `When you create a new object of a class, Python automatically calls the __init__() method to initialize the object’s attributes.`
- Naming convention: It follows the `camelCase` convention
- Naming convention: `Variables`, `Function` names are conventional and python uses `snake_case` to name them.
- Exercise: `Vehicle.py`

## Instantiating a Class
- Creating an object that is an `instance` of a class is called `instantiating` a class
    - To create an instance of a class, you use the class `name` with `parentheses`
    - Example: `v = Vehicle("Honda", "Civic", 2017)`
- In this case, `v` becomes a Honda Civic, a new instance of Vehicle

## self
- The `self` keyword refers to the `current` class instance.
- `self` must always be the `first` parameter to `__init__()` and `any` methods and properties on class instances.
- You `never` have to pass it directly when calling instance methods, including `__init__()`
- Exercise: `Comments.py`

## Underscores: Dunder Methods, Name Mangling, and More
- Example: `underscores.py`
- Questions:
    - What do `underscores` actually do ?
    - What's the significance of underscores in names?
- [Dunder Methods](https://mathspp.com/blog/pydonts/dunder-methods)
- [Name Mangling](https://www.geeksforgeeks.org/name-mangling-in-python/)

## Instance Attributes and Methods
- Example: `user_methods.py`
- Instance Attributes/Instance variables
    - Instance variables are bound to a specific instance of a class.
    - Python stores instance variables in the `__dict__` attribute of the instance. Each instance has its own `__dict__` attribute and the keys in this `__dict__` may be different.
    - When you access a variable via the instance, Python finds the variable in the `__dict__` attribute of the `instance`. If it cannot find the variable, it goes up and look it up in the `__dict__` attribute of the `class`.
- Instance Methods
    - When you define a function inside a class, it’s purely a function. However, when you call the function via an instance of a class, the function becomes a `method`. Therefore, `a method is a function that is bound to an instance of a class.`
    - A method is an instance of the method class.
    - A method has the first argument (`self`) as the object to which it is bound.
    - Python automatically passes the bound object to the method as the first argument. By convention, its name is `self`.
- Exercise: `BankAccount.py`
- Convention
    - Instance variable names should be all `lower case`
    - Words in an instance variable name should be `separated` by an `underscore`
    - `Non-public `instance variables should begin with `a single underscore`

## Class Attributes
- Example: `user_class_attributes.py`
- Example: `pet.py`
- We can also define attributes directly on a class that are `shared by all instances of a class and the class itself`.
- `Note`: If you’ve been programming in Java or C#, you’ll see that class attributes are similar to the `static members`, but not the same.
- When do we need `class attributes`?
    - storing class constants
    - tracking data across all instances
    - defining default values.
- Exercise: `ChickenCoop.py`
- Summary:
    - A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the `__init__()` method.
    - Use `class_name.class_attribute` or `object_name.class_attribute` to access the `value` of the class_attribute.
    - Use class attributes for storing class contants, track data across all instances, and setting default values for all instances of the class.

## Class Methods
- Example: `class_methods.py`
- Class methods are methods (with the `@classmethod` decorator) that are `not` concerned with `instances`, `but` the `class` itself.
- The first argument is `cls` (for class) instead of `self`. Like self, it does `not` need to be passed in explicitly.
- Class methods are `available` on the `class itself` and `any instances of the class`, and are `mostly` used for `building` new instances of classes.
- syntaxtic suger
- `class` methods vs `static` methods

## The `__repr__` method
- The `__repr__` method is one of several ways to provide a nicer string representation
- There are also several other dunders to return classes in string formats (notablu `__str__` and `__format__`), and choosing one is a bit complicated!
- Example: `repr.py`

## References
- [What is OOP?](https://www.freecodecamp.org/news/object-oriented-programming-python/?fbclid=IwAR3qiQsTbuU16kOzQGG5I45kEnJgy_gXHY1ZjWXjgBErNinyB37uRfalBHQ#what-is-oop)
- [Convention name for Class](https://peps.python.org/pep-0008/#class-names)
- [Nameming convention](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)
- [Encapsulation](https://www.pythontutorial.net/python-oop/python-private-attributes/)
- [Abstraction](https://www.freecodecamp.org/news/what-is-abstraction-in-programming/)
- [`__init__`](https://www.pythontutorial.net/python-oop/python-__init__/)
- [Instance variables](https://www.pythontutorial.net/python-oop/python-instance-variables/)
- [Class attributes](https://www.pythontutorial.net/python-oop/python-class-attributes/)
- [Class variables](https://www.pythontutorial.net/python-oop/python-class-variables/)
- [Class methods](https://www.pythontutorial.net/python-oop/python-class-methods/)
- [Private attributes](https://www.pythontutorial.net/python-oop/python-private-attributes/)
- [`__repr__`](https://www.pythontutorial.net/python-oop/python-__repr__/)