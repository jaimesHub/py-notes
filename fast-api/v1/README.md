# Setup a basic FastAPI project
- All things here I've referenced from [The FastAPI Documentation](https://fastapi.tiangolo.com/tutorial)
- This note guides you to install and implement `FastAPI` app manually with `venv` & `pip`

## Install packages in a virtual environment using pip and venv
- Create and activate `a virtual environment`
    - Create a new virtual environment: `python3 -m venv .venv`
    - Activate a virtual environment: `source .venv/bin/activate`
    - To confirm the virtual environment is activated: `which python`
    - Deactivate a virtual environment: `deactivate`
    - Reactivate a virtual environment: Back to `Activate a virtual environment` process

- Prepare `pip`
    - What: It’s used to install and update packages into a virtual environment.
    - Make sure that pip is up-to-date by running
        - `python3 -m pip --version`
        - `python3 -m pip install --upgrade pip`

- Install packages into a virtual environment using the `pip` command
    - Context: When your virtual environment is activated, you can install packages.
    - How: `pip install <package-name>`
        - Install a package (`FastAPI`)
        - [Install a specific package version](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#install-a-specific-package-version)
        - [Install extras](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#install-extras)
        - [Upgrading packages](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#upgrading-packages)
        

- Use and create a `requirements` file
    - [Using a requirements file](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-a-requirements-file)
    - [Freezing dependencies](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#freezing-dependencies)
        - The `pip freeze` command is useful for creating [Requirements](https://pip.pypa.io/en/latest/user_guide/#requirements-files) Files that can re-create the `exact` versions of all packages installed in an environment.

## Install FastAPI
- Bash: `pip install "fastapi[all]"`

## Before running code*
- [Update Python Interpreter](https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code)
- Path:
    For example: ~/Desktop/Back-To-Basic/Python-projects/py-notes/fast-api/v1/.venv/bin/python3.12

## Tutorial - User Guide
- First steps
    - Create: `main.py`
    - Run the live server: `uvicorn main:app --reload`
    - Check at your browser: `http://127.0.0.1:8000/`
    - Interactive API docs: `http://127.0.0.1:8000/docs`
    - Alternative API docs: `http://127.0.0.1:8000/redoc`
- Path Parameters
    - Path parameters & Path parameters with Type
    - Data conversion
    - Data validation
    - Documentation
        - Docs will update when user changes `Path Parameters' Types`
    - Pydatic
        - All the `data validation` is performed under the hood by `Pydantic`
    - Order Matters
        - When creating `path operations`, you can find situations where you have `a fixed path`
        - `Path operations` are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`
        - If `/users/{user_id}` is declared before `/users/me`, "thinking" that it's receiving a parameter `user_id` with a value of `me`
        - You cannot redefine a path operation
            - The first one will always be used since the path matches first
    - Predefined values
        - Create an `Enum` class
        - Declare a `path` parameter
    - Path parameters containing paths
        - OpenAPI support: no
        - Path converter: Using `Starlette`
            - `http://127.0.0.1:8000/home/johndoe/myfile.txt`
            - `http://127.0.0.1:8000/files//home/johndoe/myfile.txt`
- Query Parameters
    - Defaults
    - Optional Parameters
    - Query parameter type conversion
    - Multiple path and query parameters
        - path parameters
        - query parameters
    - Required query parameters
        - If you don't want to add a specific value but just make it optional, set the default as `None`
        - When you want to make a query parameter required, you can just not declare any default value
        - You can define some parameters as required, some as having a default value, and some entirely optional
- Request Body
    - To declare a `request` body, you use `Pydantic` models
    
## Others
- [Starting FastAPI](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2181s)
- Path Operations
- Postman
- HTTP Requests
- Schema Validation With Pydantic
- CRUD Operations

## References
- [Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments)
- [Install FastAPI](https://fastapi.tiangolo.com/tutorial/#install-fastapi)
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)