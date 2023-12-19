# Implementation of the Interface Adapters layer
- [typing module](https://docs.python.org/3/library/typing.html?highlight=typing)
    - [Dict](https://docs.python.org/3/library/typing.html?highlight=typing#typing.Dict)
- [copy module](https://docs.python.org/3/library/copy.html?highlight=copy#module-copy)
    - [deepcopy](https://docs.python.org/3/library/copy.html?highlight=copy#copy.deepcopy)
- iter
    - [Python Documentation](https://docs.python.org/3/library/functions.html?highlight=iter#iter)
    - [Iterators and Iterables in Python: Run Efficient Iterations](https://realpython.com/python-iterators-iterables/)

## The Controller
The Controller takes `user input`, converts it into `the input DTO` defined in the `Use Cases layer` and passes `this DTO` to the `Use Cases layer`.


## The Presenter
- The Presenter takes `the output DTO` from the `Use Cases layer`, converts it into a format `appropriate` for the `user` and passes it to the user. 
- For example, the Presenter will convert dates and datetimes to strings in a format appropriate for the user.

## The View
- The View receives data from the `Presenter` and `displays` it to the user.

## The Implementation
- Our implementation of `the Interface Adapters layer` is in the folders
    - [src/infra](../infra/__init__.py)
    - [src/app](../app/__init__.py)

- `src/infra`
    - Inside `src/infra` we have `Interface Adapters code` that may be used in `multiple` implementations.

    - Inside this folder we have the `repositories` folder where we have the `repository` implementations.

- `src/app`
    - In the `src/app` folder, we have code that is `specific` to each implementation.
        - The `cli_memory` folder that implements `a Command Line Interface (CLI)`
        - It uses the in-memory repository

    - Inside the `cli_memory` folder we have `controllers`, `presenters` and `views` in their respective folders.

    - Also we have the folder `interfaces` where we have `Abstract Classes` related to this layer.

- Note:
    - Besides `app` and `infra` we can find `other projects` that name the folder of this layer as `interface adapters` and `application`. 

## The Code
- The In-Memory Repository: [infra.repositories.profession_in_memory_repository.py](../infra/repositories/profession_in_memory_repository.py)

- The Repository Test: [infra.repositories.profession_in_memory_repository_test.py](../infra/repositories/profession_in_memory_repository_test.py)

- The Presenter: [app.cli_memory.presenters.create_profession_presenters.py](../app/cli_memory/presenters/create_profession_presenter.py)

- The Presenter Test: [app.cli_memory.presenters.create_profession_presenters_test.py](../app/cli_memory/presenters/create_profession_presenter_test.py)

- The Controller: [app.cli_memory.controllers.create_profession_controller.py](../app/cli_memory/controllers/create_profession_controller.py)

- The Controller Test: [app.cli_memory.controllers.create_profession_controller_test.py](../app/cli_memory/controllers/create_profession_controller_test.py)