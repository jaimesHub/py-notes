# Scope

## Global Scope
- What is it?
    - Every variable we work with in Python has a `scope` or `boundary where it can be used`.
    - There are specific rules to how variables are scoped based on where they are initially defined
- 4 main types
    - Lexical / Local
        - Variables defined in a function are `scoped to that function`
        - They are not available outside of that function
        - `local_scope.py`
    - Enclosing
        - Nested `inner` functions have access to variables declared in outer parent functions
        - `enclosing_scope.py`
    - Global
        - Variables declared outside of functions are in the global scope
        - All functions have access to them
        - `global_scope.py`
    - Built-in
        - All the built-in objects in Python are in the Built-in Scope
        - We have access to them anywhere
        - `built_in_scope.py`

## Local Scope
- Variables defined in a function are `scoped to that function`
- They are not available outside of that function
- `local_scope.py`

## Scope In Loops and Conditionals?
- `scope.py`
- How local scope works ?
- What it applied to ?
- They apply to functions
- They do not apply to Loops / Conditionals

## Enclosing Scope
- Nested `inner` functions have access to variables declared in outer parent functions
- `enclosing_scope.py`

## Built-In Scope
- All the built-in objects in Python are in the Built-in Scope
- We have access to them anywhere
- `built_in_scope.py`

## Scope Precedence Rules
- `legb.py`
- order: [built-in[global[enclosing[local]]]]

## The `global` Keyword