# Functions

## Introducing Functions
- Functions are reuseable actions that have a name
- Syntax: func_name()
- Goal: How to define, execute functions
- Why use them
    - Prevent code duplication. Keep code `DRY`
    - Abstract away code, breaking a complex program down  into small pieces
- Example: `tictactoe game`

## Our Very First Function!
- 2 processes:
    - `Define`:
        - Before we can use a function, we must define it and give it a name
        - Example: `first_function.py`
        - `def` keyword
        - indentation
    - `Execute`: 
        - Calling a function: Once Python `knows` about our function, we can call it anytime
        - Example: `first_function.py`
        - Calling it with `parentheses`

## Functions With An Input
- `first_arg.py`
- A lot of them require `an input` as an `argument`
    - def laugh(level)
    - len("string"), print("hello world")
- `level` called input/parameters
- `"string"`, `"hello world"` are arguments
    - `Arguments` are the inputs when you're running a function
    - `Parameters` are the variables that hold the argument values

## Functions With Multiple Arguments
- Arguments
    - Orders matters
- `multiple_args.py`

## Introducing Return
- Any function as machines
- len("hello") `returns` 5
- result = divide(1,2) -> result `returns` None

## Using The Return Keyword
- Outputs whatever value comes after `return` keyword -> `Ends the execution of a function`
- `return` followed by expression/value
- `return.py`

## Function Practice Set
- `practice.py`

## Default Parameters
- strip()
- To give a parameter a default value if no argument is provided, simply add the default using this format: `parameter=value`
- Example:
    ```
        def laugh(intensity=10):
            print("HA" * intensity)
    ```
- Example: `default_params.py`

## Ordering Default Parameters
- Example: `default_params.py`
- Note: parameters' order are significant

## Keyword/Named Arguments
- `keyword_args.py`
- named argument: 
    - order does not matter
- error: 
    - Non-default argument follows default argument