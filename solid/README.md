# SOLID

## Pillars of OOP
- Abstraction
    - Abstraction is a model of a real-world object or phenomenon, limited to a specific context, which represents all details relevant to this context with high accuracy and omits all the rest

    - Example

        ![Airplane class with many contexts](./assets/Screen%20Shot%202023-12-06%20at%209.36.25%20AM.png)

- Encapsulation
    - Context
        - To start a car engine, you only need to turn a key or press a button.
        - You don’t need to connect wires `under the hood`, rotate the crankshaft and cylinders, and initiate the power cycle of the engine
            - These details are `hidden` under the hood of the car.
        - You have only a simple `interface`: a start switch, a steering wheel and some pedals
            - This illustrates how each object has an `interface`—a public part of an object, open to interactions with other objects.
    - What
        - *Encapsulation* is the ability of an object to hide parts of its state and behaviors from other objects, exposing only a limited interface to the rest of the program.
    - Interfaces and abstract classes/methods in OOP
        - the `interface` mechanism (usually declared with the `interface` or `protocol` keyword) lets you define `contracts` of interaction between objects.
            - the interfaces only care about `behaviors` of objects
            - we `can’t` declare a `field` in an interface
    - Example

        ![UML diagram of several classes implementing an interface](./assets/Screen%20Shot%202023-12-06%20at%209.54.33%20AM.png)
- Inheritance
    - *Inheritance* is the ability to build new classes on top of existing ones.
    - The main `benefit` of inheritance is code `reuse`
        -  you `extend` the `existing class` and put the `extra` functionality into a resulting `subclass`, which inherits fields and methods of the superclass.
        - The consequence of using inheritance is that subclasses have the same interface as their parent class
    - UML diagram

        ![UML diagram of extending a single class versus implementing multiple interfaces at the same time](./assets/Screen%20Shot%202023-12-06%20at%2011.14.31%20AM.png)

- Polymorphism
    - Example
        - Most `Animals` (class) can make sounds.
            - therefore we can declare `makeSound()` method abstract right away
        - All `subclasses` will need to `override` the base `makeSound()` method
            - UML Diagram

                ![Animal class](./assets/Screen%20Shot%202023-12-06%20at%2011.19.25%20AM.png)
    - What
        - `Polymorphism` is the `ability` of a program to `detect` the real class of an object and `call` its `implementation` even when its real type is `unknown` in the current context.
            - You can also think of polymorphism as the ability of an object to `“pretend”` to be something else, usually a `class` it `extends` or an `interface` it `implements`. 
            - In our example, the `dogs` and `cats` in the bag were `pretending` to be `generic animals`.

## Relations Between Objects*
- While we talk about `relations` between `objects`, keep in mind that `UML` represents relations between `classes`.

- Dependency: is the most `basic` and the `weakest` type of relations between classes

    ![UML diagram Dependency](./assets/Screen%20Shot%202023-12-06%20at%2011.26.04%20AM.png)

- Association: is a `relationship` in which `one` object `uses` or `interacts` with `another`

    ![UML diagram Association](./assets/Screen%20Shot%202023-12-06%20at%2011.27.56%20AM.png)

- Aggregation: is a `specialized type of association` that represents `“one-to-many”`, `“many-to-many”` or `“whole-part”` relations between `multiple` objects.

    ![UML diagram Aggregation](./assets/Screen%20Shot%202023-12-06%20at%2011.38.37%20AM.png)

- Composition: is a `specific kind of aggregation`, where `one` object is `composed` of `one or more instances of the other`.
    - The most notorious example for this is the famous principle `“choose composition over inheritance.”`
    - UML Diagram

    ![UML diagram Composition](./assets/Screen%20Shot%202023-12-06%20at%2011.46.16%20AM.png)

- Recap
    - UML diagram

        ![Relations between objects and classes: from weakest to strongest](./assets/Screen%20Shot%202023-12-06%20at%209.25.32%20AM.png)
    
    - `Dependency`: Class А can be affected by changes in class B.
    - `Association`: Object А knows about object B. Class A depends on B.
    - `Aggregation`: Object А knows about object B, and consists of B. Class A depends on B.
    - `Composition`: Object А knows about object B, consists of B, and manages B’s life cycle. Class A depends on B.
    - `Implementation`: Class А defines methods declared in interface B. Objects A can be treated as B. Class A depends on B.
    - `Inheritance`: Class А inherits interface and implementation of class B but can extend it. Objects A can be treated as B. Class A depends on B.

## Software Desing Principles**
- Features of Good Design
- Code reuse
    - Cost and time are two of the most valuable metrics when developing any software product
    - Code reuse is one of the most common ways to reduce development costs.
        - Instead of developing something over and over from scratch, why don’t we reuse existing code in new projects?
        - It takes extra effort
            - `Tight coupling` between components
            - Dependencies on `concrete` classes instead of `interfaces`
            - Hardcoded operations
- Extensibility
    > There’s a bright side: if someone asks you to change something in your app, that means someone still cares about it.

    - `Change` is the only constant thing in a programmer’s life
    - That’s why all seasoned developers try to provide for `possible future changes` when `designing` `an application’s architecture`
    

## Design Principles**
- Questions:
    - What is good software design?
    - How would you measure it?
    - What practices would you need to follow to achieve it?
    - How can you make your architecture flexible, stable and easy to understand?

- Encapsulating
    > Identify the aspects of your application that vary and separate them from what stays the same

    - The main goal of this principle is to minimize the effect caused by changes.
    - Example
        - BEFORE: tax calculation code is mixed with the rest of the method’s code

            ![BEFORE](./assets/Screen%20Shot%202023-12-06%20at%2012.21.22%20PM.png)

        - AFTER: you can get the tax rate by calling a designated method.

            ![AFTER](./assets/Screen%20Shot%202023-12-06%20at%2012.22.22%20PM.png)

- Program to an Interface, not an Implementation
    > Program to an interface, not an implementation. Depend on `abstractions`, `not` on `concrete classes.`

- Favor Composition Over Inheritance
    - `Problem`: `inheritance` comes with caveats that often become apparent only after your program already has `tons of classes` and `changing` anything is pretty `hard`.
        - A subclass can’t reduce the interface of the superclass.
        - When overriding methods you need to make sure that the new behavior is compatible with the base one.
        - Inheritance breaks encapsulation of the superclass
        - Subclasses are tightly coupled to superclasses
        - Trying to reuse code through inheritance can lead to creating parallel inheritance hierarchies.
    - That's why `Composition` comes in
        - Inheritance represents the `“is a”` relationship between classes (a car is a transport)
        - Composition represents the `“has a”` relationship (a car has an engine).

## Solid principles*

- `S`ingle Responsibility Principle
    > A class should have just one reason to change.

- `O`pen/Closed Principle
    > Classes should be open for extension but closed for modification

- `L`iskov Substitution Principle
    > When extending a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the client code.

- `I`nterface Segregation Principle
    > Clients shouldn’t be forced to depend on methods they do not use

- `D`ependency Inversion Principle
    > High-level classes shouldn’t depend on low-level classes. Both should depend on abstractions. Abstractions shouldn’t depend on details. Details should depend on abstractions.

## Recap

## References
- [Book: Dive Into Design Pattern](https://refactoring.guru/design-patterns/book)
    - Part: Introduction to OOP
    - Part: Software Design Principles
    - Part: Design Principles
    - Part: SOLID Principles