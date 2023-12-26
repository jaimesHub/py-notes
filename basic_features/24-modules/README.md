# Modules

## Working With Built-In Modules
- A module is simply a Python file that contains code that can be re-used in other files
- Modules allow us to break up `complex` programs into `smaller`, more `manageable` pieces across multiple files.
- 3 types:
    - Built-in
    - Custom
    - 3rd Party
- Standard Library
    - [Standard Library](https://docs.python.org/3/library/)
    - Python comes with tons of built-in modules that we can use, `if we import them.`
    - Each module consists of methods and functionality bundled together
    - To use a module, we must import it first using the `import` keyword
        > import random
        > random.randint(1,6)
        3
    - `import.py`

## Importing More Built-In Modules
- `calendar.py`

## Fancy Import Syntax
- `import as`: use the `as keyword` to import a module and give it a custom name in your script
    - `import_as.py`
- `from...import`: use the `from <module> import <method>` syntax to import specific pieces of a module
    - `from_import.py`
    - we can import multiple methods
- `import *`
    - `from_import.py`
    - We can import all pieces of a module individually using `import *` however this usually is not the best approach to importing

## Creating Custom Modules
- `custom_modules`

## 3rd Party Modules: Pip & PyPI
- pip is `the Python package installer` that we can use to install hundreds of thoudsands of packages for use in our projects. (~ same as npm/yarn/pnpm)
- syntax: `python3 -m pip install <package>`
- [Installing PIP](https://docs.python.org/3/installing/index.html)

## Our First Pip Package
- python -m pip install art
- `ascii_art.py`

## Language Translator Package
- python -m pip install translate
- `greeter.py`

## Sentiment Analysis Fun Project Installation

## Sentiment Analysis Fun Project