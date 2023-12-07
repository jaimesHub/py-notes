# Dependency Inversion Principle (DIP)

## What
- The Dependency Inversion Principle (DIP) states that:
    - `High-level modules` should not depend on `low-level modules`. `Both` should `depend` on `abstractions`.
    - `Abstractions` should `not` depend on `details`. `Details` should depend on `abstractions`.

## Why (objectives)
- To reduce `coupling` by implementing an abstraction layer
    - It becomes loosely coupled as there is no direct dependency and the dependency is now on an abstraction, not the implementation class.
- Example
    - The `main application` is using the `Storage` abstraction to save data to `MySQL` and/or a `CSV file`.
    - This relationship is loosely coupled as we can easily switch if we want to save the data in the MySQL database or a CSV file or even both.
    - `Business rules` or `use cases` only require that the `data` is `safely` stored.
        - They do `not` have to know `where` it is stored or `how` it is implemented.
    - Diagram

        ![Diagram](../../../assets/Screen%20Shot%202023-12-07%20at%2010.51.41%20AM.png)

## Example in Code
- Problem: `ViolateDIP.py`
- Solution: `FollowDIP.py`

## Conclusion
- Following the Dependency Inversion Principle we can `improve` our code `maintainability` and `flexibility` because it will depend less on lower classes (like `MySQLStorage` in our example) and we can even use `more` than one lower class `without` changing the higher class (e.g. UseCase).  
