# Implementation of the Use Cases layer

- dataclasses
    - [@dataclass](https://www.pythontutorial.net/python-oop/python-dataclass/)
    - [asdict](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict)
    
- implement interfaces in Python
    - [Python Abstract Classes](https://www.pythontutorial.net/python-oop/python-abstract-class/)
    - [Python Interface](https://realpython.com/python-interface/)
    - [Python Multiple Interfaces](https://pythonguides.com/python-interface/#Python_multiple_interfaces)
    - [Difference between interface and abstracts](https://discuss.python.org/t/difference-between-interface-and-abstracts/33315)

## Data Transfer Object (DTO)
- DTO is a data object used to `transfer data` from one layer to another
- Its advantages
    - It `reduces` the number of parameters when we use a DTO with several data as a parameter instead of passing several parameters.
- They contain `no` business logic
    - it is possible to not use Data Transfer Objects (DTOs) and pass the data as parameters, `especially` in cases with few parameters.

## The implementation
- `src/interactor` folder
    - `dtos` folder
        - we use a DTO with several data as a parameter instead of passing several parameters.
        - locate: [interactor.dtos](./dtos/__init__.py)

    - `interfaces` folder: 
        - where we have `Abstract Classes` referenced by the `use cases`
        - locate: [interactor.interfaces](./interfaces/__init__.py)

    - `use_cases` folder: 
        - where we have the `use cases`
        - locate: [interactor.use_cases](./use_cases/__init__.py)

- Note: Besides `interactor` and `use cases`, we can find other projects that name the folder of `this layer` as `app`, `domain` and `application`

- Why do we need to use `Abstract Classes` ?
    - as it is `not` required
    - but
        - defining it will `reduce` future problems
        - make the code `easier` to understand

## The Code
- The DTOs: [interactor.dtos.create_profession_dtos.py](./dtos/create_profession_dtos.py)

- The Repository Interface: [interactor.interfaces.repositories.profession_repository.py](./interfaces/repositories/profession_repository.py)

- The Presenter Interface: [interactor.interfaces.presenters.create_profession_presenter.py](./interfaces/presenters/create_profession_presenter.py)

- The Use Case: [interactor.use_cases.create_profession.py](./use_cases/create_profession.py)

- The Use Case Test: [interactor.use_cases.create_profession_test.py](./use_cases/create_profession_test.py)