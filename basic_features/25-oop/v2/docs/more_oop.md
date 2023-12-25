# More OOP

## Inheritance
- A key feature of OOP is the ability to define a class which `inherits` from another class (a `base` or `parent` class).
- In Python, inheritance `works` by passing the `parent` class as an `argument` to the definition of a `child` class
- Example: `simpler_inheritance.py`
- `isinstance()`
- All about properties
    - Example: `human.py`
    - The problem that properties can help us solve is that a user can just directly or code can directly change attribute (`age` for example) -> make use of a `property` -> `@property`
    - `@getter_func_name.setter`

## super
- The `super()` keyword allows us to `call` the `__init__` function of a `parent` class
- example: `animal.py`
- Recap
    - `super()` -> reduce duplication
- More example: `user_2.py`

## Exercise:
- File: `exercises/roleplay_game`

## Multiple Inheritance
- Python also allows classes to inherit from `more` than one parent class
- Example: `animals.py`

## Method Resolution Order (MRO)
- Whenever you create a class, Python sets a `Method Resolution Order`, or `MRO`, for that class, which is the order in which Python will look for methods on instances of that class.
- You can programmatically reference the MRO three ways:
    -  `__mro__` attribute on the class 
    -  use the `mro()` method on the class 
    - use the builtin `help(cls)` method
- Example: `mro.py`

## Exercise
- `oop/v2/exercises/mro_genetics`

## Polymorphism
- A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph).
- While a formal definition of polymorphism is more difficult, here are two important practical applications
    - The `same` class method works in a `similar` way for `different` classes
        ```
            Cat.speak() # meow
            Dog.speak() # woof
            Human.speak() # yo
        ```
    - The `same` operation works for `different` kinds of objects
        ```
            sample_list = [1,2,3]
            sample_tuple = (1,2,3)
            sample_string = "awesome"

            len(sample_list)
            len(sample_tuple)
            len(sample_string)
        ```

## Polymorphism & Inheritance
### The same class method works in a similar way for different classes
- A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called `method overriding`.
    - Each `subclass` will have a `different` implementation of the method.
    - If the method is `not` implemented in the subclass, the version in the `parent` class is called instead.
    - Example: `animals_2.py`

### (Polymorphism) The same operation works for different kinds of objects
- Python classes have special (also known as "`magic`") methods, that are `dunders` (i.e. double underscore-named). 
- These are methods with special names that give instructions to Python for how to deal with objects.

## Special Methods Example
- Example: `special_methods.py`
- The `+` operator is shorthand for a special method called `__add__()` that gets called on the first operand.
- If the first (left) operand is an instance of `int`, `__add__()` does `mathematical` addition. If it's a `string`, it does `string` concatenation.

### Special Methods Applied
- Therefore, you can declare `special` methods on `your own classes` to `mimic` the `behavior` of builtin objects

### String Representation
- The `most common` use-case for special methods is to make classes "`look pretty`" in strings.
- The `__repr__` method is one of several ways to provide `a nicer string representation`
- There are also `several other dunders` to return classes in `string` formats (notably `__str__` and `__format__`), and choosing one is [a bit complicated!](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr)

### Making a Grumpy Dictionary - Overriding Dict
- Example: `grumpy.py`
- https://docs.python.org/3/reference/datamodel.html

## Exercise
- `oop/v2/exercises/special_methods_train`

## Reference
- [Inheritance Python Documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Inheritance](https://www.pythontutorial.net/python-oop/python-inheritance/)
- [Super Python Documentation](https://docs.python.org/3/library/functions.html#super)
- [Super()](https://www.pythontutorial.net/python-oop/python-super/)
- [Multiple Inheritance](https://www.pythontutorial.net/python-oop/python-multiple-inheritance/)
- [mro](https://docs.python.org/3/library/stdtypes.html?highlight=mro#class.mro)
- [Special Methods](https://docs.python.org/3/reference/datamodel.html)