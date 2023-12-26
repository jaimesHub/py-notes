# QUIZZ

## Question 1
Say we have a class Pet :

    class Pet(Animal, Friend):
        def __init__(self, name)
            self.name = name

What is the best way to call the parent `__init__` methods?

-> In the init method, call `super().__init__`
-> Because: Super is the preferred way to reference the parent since it follows MRO automatically

## Question 2
What is MRO in Python?
-> The order in which Python looks up (aka resolves) methods on a class, influenced by inheritance

## Question 3
What are three ways to look up MRO for the class `Penguin` ?
-> 3 ways
Penguin.`__mro__`
Penguin.mro()
help(Penguin)

## Question 4
```   class Animal:    
        def speak():
            raise NotImplementedError
```

Why is it considered good OOP practice for Animal  to raise a NotImplementedError ?
-> It's impossible to generalize a sound that all animals make, therefore it's best left up to the subclasses to implement.

## Question 5
```
    5 + 5 = 10
    "5" + "5" = "55"
```
How does Python know how to interpret the `+` operator differently in these cases?  
-> The first argument has special method that defines what to do with the `+` operator
-> the actual operation Python performs is something like x.`__add__`(y)

## Question 6
```
    class ShoppingCart:
        def __init__(self):
            self.items = []
            self.count = 0
```
How can I make it so that `len(cart)` returns the `count` of items in my shopping cart, provided cart  is an instance of ShoppingCart ?
-> Add `self.__len__(self)` as a new method on ShoppingCart that returns `self.count`
-> in other words implement the special/magic/dunder method `__len__()` which the builtin len calls.