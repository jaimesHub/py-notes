# v2/clean-architecture

## Github links
- [branch::v2/clean-architecture](https://github.com/jaimesHub/py-notes/tree/v2/clean-architecture/clean-architecture/v2)

1. `Entities` layer: v2/src/domain
- [value_objects.py](./src/domain/value_objects.py)
- [post.py](./src/domain/entity/post.py)
- [post_test.py](./src/domain/entity/post_test.py)

2. `Use Cases` layer: v2/src/interactor
- [dtos](./src/interactor/dtos/)
- [interfaces](./src/interactor/interfaces/) folder: where we have `Abstract Classes` referenced by the use cases
    - [repositories](./src/interactor/interfaces/repositories/)
    - [presenters](./src/interactor/interfaces/presenters/)
    - [use_cases](./src/interactor/use_cases/) folder: where we have the use cases
- Note: 
    - `other` projects can have: app, domain, application
    - We can implement a Clean Architecture without using `Abstract Classes`
    - But defining it will reduce future problems and make the code easier to understand

3. `Interface Adapters` layer:
- [src/infra](./src/infra/): where we have `Interface Adapters code` that maybe used in `multiple` implementations
    -[src/infra/repositories](./src/infra/repositories/)

- [src/app](./src/app/)
    - [src/app/cli_memory](./src/app/cli_memory/)
        - [interfaces](./src/app/cli_memory/interfaces/)
        - [presenters](./src/app/cli_memory/presenters/)
        - [views](./src/app/cli_memory/views/)
        - [controllers](./src/app/cli_memory/controllers/)

- [main.py]

- Note: Besides `app` and `infra` we can find `other` projects that name the folder of this layer as `interface adapters` and `application`.

