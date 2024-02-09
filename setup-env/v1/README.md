# Setting Up VSCode For Python: A Complete Guide

## Python and Visual Studio Code Setup

### Installing Python
Go to [Python.org](https://www.python.org/downloads/) and download the latest version

### Installing VSCode
Download and install the stable build from the [official website](https://code.visualstudio.com/)

### Running Python in VSCode
- Select the Python interpreter
- To run the Python file, simply click on the Run button on the top left
- Or type: `python3 *file_name*.py`

## Installing Essential VSCode Python Extensions

### How to install a VSCode Extension
- Click on the box icon on `the activity bar` or use a `keyboard shortcut`: `Ctrl + Shift + X` to open the extension panel. 
- Type: `Python`

### List of Essential Python Extensions 

#### 1. Python
- The [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension automatically installs [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), and [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) extensions.

    - `Pylance` is the default language server for Python in VS Code, and is installed alongside the Python extension to provide `IntelliSense` features.

    - [Enable Auto Imports](https://code.visualstudio.com/docs/python/editing#_enable-auto-imports)

    - [Quick Fixes](https://code.visualstudio.com/docs/python/editing#_quick-fixes)

- Key features
    - Code autocomplete: [IntelliSense](https://code.visualstudio.com/docs/python/editing#_autocomplete-and-intellisense)

    - `Pylint`/Flake8: [Linting](https://code.visualstudio.com/docs/python/linting)
        - Linting highlights `syntactical and stylistic problems` in your Python source code, which often helps you `identify` and `correct` subtle programming `errors` or `unconventional coding practices` that can lead to errors.
    
    - `black`/autopep: [Code formatting](https://code.visualstudio.com/docs/python/editing#_formatting)
        - [Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
    
    - [Debugging](https://code.visualstudio.com/docs/python/debugging)

    - unittest/pytest: [Testing](https://code.visualstudio.com/docs/python/unit-testing)

    - `venv`/`pipenv`/conda: [Environment](https://code.visualstudio.com/docs/python/environments)

    - [Refactoring](https://code.visualstudio.com/docs/python/editing#_refactoring)

#### 2. Indent-rainbow
[Indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) extensions provide us with a multilevel colorized indentation for improved code readability.

#### 3. Python Indent
[Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) extension helps us with creating indentations.

#### 4. autoDocstring
The [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extension helps us quickly generate docstring for Python functions.

### Configuring Linting and Formatting in `VSCode`

#### Linting
- [Linting](https://code.visualstudio.com/docs/python/linting)
    - highlights the problems in the Python source code and provides us with suggestions.
    - it generally highlights syntactical and stylistic issues.
    - it helps you identify and correct coding issues that can lead to errors.
- [List of available linting methods](https://code.visualstudio.com/docs/python/linting#_specific-linters)

#### Formatting
- Formatting makes code readable. 
- It follows specific rules for line spacing, indents, spacing around operators, and closing brackets.
- [PEP-8: Python Naming Conventions & Code Standards](https://www.datacamp.com/tutorial/pep8-tutorial-python-code)
    - learn Python's style guide and formatting rules
- Format On Save

### Debugging and Testing in VSCode
- [Debugging](https://www.datacamp.com/tutorial/setting-up-vscode-python#debugging-thepy)
- [Testing](https://www.datacamp.com/tutorial/setting-up-vscode-python#testing-thepy)

### Git Integration
- [Git Integration](https://www.datacamp.com/tutorial/setting-up-vscode-python#git-integration-vscod)

### Tips and Tricks for Effecient Python Development in VSCode
- [Tips and Tricks for Efficient Python Development in VSCode](https://www.datacamp.com/tutorial/setting-up-vscode-python#tips-and-tricks-for-efficient-python-development-in-vscode-vscod)
- Sync your settings by logging into your GitHub account. It will sync your settings across all of the machines. 

## References
- [Setting up VSCode in Python](https://www.datacamp.com/tutorial/setting-up-vscode-python)
- [PEP-8: Python Naming Conventions & Code Standards](https://www.datacamp.com/tutorial/pep8-tutorial-python-code)