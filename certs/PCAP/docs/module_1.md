# Module 1: Introduction to Modules

## Modules
### What is a module?
- Computer code has a tendency to grow.
- Code that doesn't grow is probably completely unusable or abandoned. 
- When the code being created is expected to be really big, you may want to divide it into many parts, implemented in parallel by a few, a dozen, several dozen, or even several hundred individual developers.
- `decomposition` process is
    - Each of these parts can be (most likely) divided into smaller ones, and so on.
- `Modules` help us to divide a piece of software into separate but cooperating parts

- The [Python Tutorial](https://docs.python.org/3/tutorial/modules.html) defines it as `a file containing Python definitions and statements, which can be later imported and used when necessary.`

### How to make use of a module?

- The handling of modules consists of two different issues (cases)
    - the module's `user`
        - it happens when you want to use an already existing module, written by someone else, or created by yourself during your work on some complex project
    - the module's `supplier`
        - it occurs when you want to create a brand new module, either for your own use, or to make other programmers' lives easier

- Python standard library
    - a special sort of library where modules play the roles of books (we can even say that folders play the roles of shelves).
    - If you want to take a look at the full list of all `volumes` collected in that library, you can find it here: https://docs.python.org/3/library/index.html.

- Each module consists of entities (like a book consists of chapters).
- These entities can be functions, variables, constants, classes, and objects. 
- For example: `math` module
    - the module contains a rich collection of entities (`not` only functions)
    - These `entities` enable a programmer to effectively implement calculations demanding the use of mathematical functions, like *sin()* or *log()*.

### Importing a module
- To make a module usable, you must `import` it (think of it like of taking a book off the shelf).
    - Importing a module is done by an instruction named `import`.
- Example: [import_example.py]


#### Namespace
- A namespace is a space (understood in a non-physical context) in which some names exist and the names don't conflict with each other
- Example

- Inside a certain namespace, each name must remain unique

- If the module of a specified name `exists and is accessible` (a module is in fact `a Python source file`), Python imports its contents, i.e., `all the names defined in the module become known, but they don't enter your code's namespace.`
    - This means that you can have your own entities named `sin` or `pi` and they won't be affected by the import in any way.

- way to enter a module's namespace
    - import math

- qualify entities' name with its originating module after using `import`
    - math.pi
    - math.sin

#### How the namespaces (yours and the module's one) can coexist?
- Example: [coexist.py](../code/coexist.py)
- As you can see, the entities don't affect each other.

#### Using *, the `as` keyword
- `from module import *`

- the list of entities' names is replaced with `a single asterisk(*)`
    - it imports `all` entities from the indicated module.
    - it relieves you of the duty of enumerating all the names you need.
    - unless you know all the names provided by the module, `you may not be able to avoid name conflicts`.
    - Treat this as a `temporary` solution, and try not to use it in regular code.

- If you use the import module variant and you don't like a particular module's name, you can give it any name you like - this is called `aliasing`.
    - `import module as alias`
    - The `module` identifies the original module's name while the "alias" is the name you wish to use instead of the original.

- Example:
    - [coexist_1.py](../code/coexist_1.py)
    - [coexist_2.py](../code/coexist_2.py)

- Note: after successful execution of an aliased import, the `original` module name becomes `inaccessible` and must `not` be used.
- The phrase `name as alias` can be repeated - use commas to separate the multiplied phrases
    - `from module import n as a, m as b, o as c`

# Recap
- modules, import module, handling of modules
- constants/functions in the moduled modules called `entities`
- namespace, asterisk (*), alias

# References
- [Python Tutorial](https://docs.python.org/3/tutorial/modules.html)
- [Python standard library](https://docs.python.org/3/library/index.html.)

