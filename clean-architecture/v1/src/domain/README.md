# The Implementation
- Our implementation of the Entities layer is in the folder `src/domain`

## Value Object
- It represents a value that `doesn't have identity` and is `immutable`
    - When we compare 2 values objects, we are comparing their values, not their identities
    - Example: if we compare two `Money` objects, we are comparing if each one `values` five dollars, not if they are the same five dollar `bill`.

- Value objects provide context
    - It means that a Money Value Object not only has the number five, but also the `currency` US dollar.

- Its advantage: we can centralize the `type` definition and `validation` on the Value Object definition

- [Example in CSharp](https://github.com/kikutano/CleanArchitecture.Template/tree/main/CleanArchitecture.Domain/ValueObjects)

## Our implementation of `the Entities layer` is implemented here

- The Value Object: 
    - `value_objects.py` file where we have the `Value Objects`

- The Entity: `entities` folder where we have the `entities`
    - [`profession.py` file](./entities/profession.py)
    - [`profession_test.py` file](./entities/profession_test.py)
    - `__init__.py` file

- [`__init__.py` file](https://www.w3docs.com/snippets/python/what-is-init-py-for.html)

- Note: Besides `domain` and `entities`, we can find `other` projects that name the layer folder as `data`.

## Steps

- The `profession`'s Value Object file: [value_objects.py](./value_objects.py)
- The `profession` Entity file: [src/domain/entities/profession.py](./entities/profession.py)
- The `profession` Entity Test file: [src/domain/entities/profession_test.py](./entities/profession_test.py)

## References
- [What is `__init__`.py file in Python](https://www.python-engineer.com/posts/init-py-file/)
- [What are `@dataclass`, `@classmethod`](https://realpython.com/primer-on-python-decorators/#decorating-classes)
