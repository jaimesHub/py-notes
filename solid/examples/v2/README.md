# Learn from Academind: SOLID

## Understanding `Cohesion`
- `Following description in v1`: In programming, cohesion has a relation to the Single Responsibility Principle (SRP). The more responsibilities that a class has, the lower its cohesion will be, and a class that follows the Single Responsibility Principle has high cohesion. [1]

- Cohesion in the end just defines `how well` the methods of a class are using the class properties
    - How much are your class methods using the class properties ? -> That's what makes up cohesion
        - `maximum` cohesion
            - You would have `maximum cohesion` inside of a class if `all methods each use all properties`
            - If that's what you would have then you would have `a highly cohesive object` and you would have maximum cohesion
        - `no` cohesion
            - It means, `all the methods don't use any class property`. So all the class properties are not managed by your methods. Instead, they probably are public and can be used from outside the class
            - Then in the end, you would just have `a Data structure/container with some utility methods `, since the methods are not operating on the properties of the class at all
    - How to avoid having a class with no cohesion unless you wanna have a data container with utility methods

- The `goal` is high cohesion 
    - we should write `highly cohesive classes` where all your methods use many of your properties, not `maximum` or `no` cohesion
    - Example: `cohesion.py`

## Coupling
- Coupling is the degree of interdependence between software parts. 
- To avoid coupling, each part of the software should work with a different part of the process. 
    - If `data` is transferred `directly` from one class to another, the `coupling` is `tight`. 
    - However, if there is an `interface` between them, then it is `loosely coupled`. It is impossible to eliminate coupling completely, so we should do it as loosely as possible.
- As a result of tightly coupled classes, if we want to make changes to the called class, we need to make changes to the other.

## The SOLID Principles

## The Single-Responsibility-Principle (SRP) & Why It Matters
- What
    - It states that "Classes should have `a single responsibility` - a class shouldn't `change for more than one reason`"
    - If a class would have multiple responsibilites, there would be multiple reasons for code edits to be made to this class, simply because it has too many responsibilites
    - A single responsibility means that code changes have less impact on the class, and the class is really focused and small

- What exactly is a single responsibility?
    - keeping classes small and not doing too many things
    - `large_class.py`
    - `violate_srp.py`

- SRP & Clean code
    - Restricting classes to one core reponsibility leads to smaller classes
    - Smaller classes tend to be easier to read
        - Make managing your code and reading your code easier
        - Example: `small_class.py`

## The Open-Closed Principle (OCP) & Why It Matters
- What
    - It states that "A class should be `opent for extension` but `closed for modification`
    - Example: `ocp.py`
    - It relates to "Polyphormism"

- Why does OCP help us with clean code
    - Extensibility ensures small class (instead of growing classes) and can help prevent code duplication (DRY)
    - Smaller classes and DRY code increase readability and maintainability

- How
    - There is no explicit `interface` keyword in Python for establishing an interface
    - In Python, an abstract class with solely abstract method is used to construct an interface
    - 2 ways
        - Informal interface
        - Metaclass
        - Formal interface: implement it using `the ABC module`
            - Abstract Base Class

## The Liskov Substitution Principle
- What
    - It states that "Objects should be `replaceable` with `instances of their subclasses without altering the behaviour.`"
    - Example: `violate_lsp.py`
    - Example: `follow_lsp.py`

- In a real application, we could have different databases. No matters if it's an SQL or a MongoDB database, we should have a `connect` method which always has the same behavior of connecting to that DB

- This principle wants to ensure that you don't model your data in the wrong way

- Recap
    - If a class inherits from another class, then you need to be able to replace that other super class with instances of inheriting class without changing any behavior.

    - It forces you to model your data correctly

## The Interface Segregation Principle
- An interface is a description of behaviors that an object can do
    - For example, when you press the power on the TV remote control, it turns the TV on, and you don't need to care how

- In OOP, `interface` is a set of methods that an object must-have
    - Its purpose is to allow client to request the correct methods of an object via its interface
    - Interfaces are constracts which forces classes to implement certain behaviors
    - `interfaces vs classes/objects/instances`

- Python uses `abstract classes` as interfaces

- It states that "`Many client-specific interfaces` are `better` than one general purpose interface"
    - We should avoid `general purpose` interfaces when following the ISP (`isp_violation.py`)
    - Instead we should have multiple smaller `clients-specific` interfaces (`isp_following.py`)

## The Dependency  Inversion Principle

- It states that "You should `depend upon abstractions, not concretions`"

## Summary
- If you use class or using Project Oriented approach, you should consider to use SOLID

## References
- SRP
    - [1](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/)

- OCP
    - [2](interface in python - abstract class)
        - [2.1](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/)
        - [2.2](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)
        - [2.3. Difference Interface and Abstrac Class](https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-python/)
        - [2.4](https://dotnettutorials.net/lesson/interfaces-in-python/)
        - [2.5. Python Abstract Class](https://www.pythontutorial.net/python-oop/python-abstract-class/)

- LSP
    - [3](lsp in python)
        - [3.1](https://www.pythontutorial.net/python-oop/python-liskov-substitution-principle/)
        - [3.2](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/)

- ISP
    - [4](isp in python)
        - [4.1](https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/)
        - [4.2](https://www.linkedin.com/pulse/python-recommended-coding-practices-part-3-solid-watanabe/)

- DIP
    - [5](dip in python)
        - [5.1](https://www.pythontutorial.net/python-oop/python-dependency-inversion-principle/)