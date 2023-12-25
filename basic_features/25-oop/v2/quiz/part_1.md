# QUIZ
## Question 1: What's the difference between a class and an instance?
- A class is a blueprint for constructing objects; an instance is an object constructed from the class definition

## Question 2: What is encapsulation in OOP?
- Encapsulation is the process of designing a programmatic class using public and private methods and attributes to implement abstraction.

## Question 3: What is abstraction in OOP?
- The idea of exposing only `relevant` data in a class interface, hiding private attributes and methods (aka the `inner workings`) from users

## Question 4: Given the following code snippet, how do we make a new instance of `Car` ?
'''
class Car():
    def __init__(self, make):
        self.make = make
'''
- `honda = Car("honda")`

## Question 5: What's the difference between a `class method` and an `instance method`?
- A class method has class(`cls`) as the implicit first argument whereas instance method has the instance (called `self`)
- Class methods must be decorated with `@classmethod`, whereas instance methods don't
- Class methods are used when the method does not need to know about the specific instance; instance methods are the opposite.