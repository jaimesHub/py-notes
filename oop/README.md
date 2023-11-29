# OOP

## Introducing OOP
- a way of organizing code
- WTF is OOP
    - OOP is an approach to programming that involves modeling `things` into Python objects
    - These objects can contain both `data` AND `functionality` all wrapped up together into a reusable component
    - `Chess`: Board/Piece/Player/AIPlayer/Match
    - Class
        - Classes are `blueprints` or `recipes` that we can later use to create objects from
        - A class describes what `properties` and `functionality` individual objects will contain
        - a pattern
    - Instance
        - we call the individual objects that are created from a class blueprint `instances`
        - what it looks like (`using pattern`)
    - Visualize example

## Class Syntax
- `puppy.py`
- define "class" 
    - with Class Name is Capitalized
        - define "def"
            - special `__init__` method `automatically` called whenever `new Puppy is created` (instatiating)
                - self: 
                    - refers to the `current` instance of class (Puppy)
                    - it must be the `first` parameter to init
                - other parameters

- instatiating
    - to create a Puppy instance, call Puppy() and provide a name
    - `__init__`  method runs first

## Writing Out First Class
- `puppy.py`

## Instance Methods
- define a function inside a class
- starting `def`, then `self` (required), other parameters if needed
- `puppy.py`

## Practicing Instance Methods
- `dog.py`
- Each `Puppy` instance is a different object

## Class Attributes
- are attributes that are defined on the class itself and they are shared across all instances of the class
- if you define a variable just floating inside of a class, that variable belongs to the class. It is a class attribute
    - all instances of `Puppy` will have (share) the `same` value for `species`
- `class_attributes.py`

## Class Methods
- We can define methods that are available on the class directly.
- These class methods are not concerned with a specific instance of the class.
- `@classmethod` decorator
- `class_method.py`

## Inheritance Basics
- `inheritance.py`

## The super() Function
- `super_method.py`
- use `super()` to refer to the `base` or `parent` class
- in this case, we use super() to access the __init__ method on from the Cat class