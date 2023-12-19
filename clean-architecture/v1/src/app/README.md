# Implementation of the Interface Adapters layer
- typing 
    - Dict
- copy
    - deepcopy
- iter

## The Controller
The Controller takes `user input`, converts it into `the input DTO` defined in the `Use Cases layer` and passes `this DTO` to the `Use Cases layer`.


## The Presenter
- The Presenter takes `the output DTO` from the `Use Cases layer`, converts it into a format `appropriate` for the `user` and passes it to the user. 
- For example, the Presenter will convert dates and datetimes to strings in a format appropriate for the user.

## The View
- The View receives data from the `Presenter` and `displays` it to the user.

## The Implementation
- Our implementation of `the Interface Adapters layer` is in the folders `src/app` and `src/infra`.
- `src/app`
    - In the `src/app` folder, we have code that is `specific` to each implementation.
        - The `cli_memory` folder that implements `a Command Line Interface (CLI)`
        - It uses the in-memory repository
    - Inside the `cli_memory` folder we have `controllers`, `presenters` and `views` in their respective folders.
    - Also we have the folder `interfaces` where we have `Abstract Classes` related to this layer.
- `src/infra`
    - Inside `src/infra` we have `Interface Adapters code` that may be used in `multiple` implementations.
    - Inside this folder we have the `repositories` folder where we have the `repository` implementations.

## The Code
- The In-Memory Repository: `clean-architecture/v1/src/infra/repositories/profession_in_memory_repository.py`
- The Repository Test: `clean-architecture/v1/src/infra/repositories/profession_in_memory_repository_test.py`
- The Presenter: `clean-architecture/v1/src/app/cli_memory/presenters/create_profession_presenters.py`
- The Presenter Test: `clean-architecture/v1/src/app/cli_memory/presenters/create_profession_presenters_test.py`
- The Controller: `clean-architecture/v1/src/app/cli_memory/controllers/create_profession_controller.py`
- The Controller Test: `clean-architecture/v1/src/app/cli_memory/controllers/create_profession_controller_test.py`