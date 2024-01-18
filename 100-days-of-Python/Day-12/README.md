# Day 12: Scope & NUmber Guessing Game

## Namespaces: Local vs. Global Scope
- real example
    - a tree and a house are rounded by a fence
    - a tree is out of this fence
- [start](https://replit.com/@appbrewery/day-12-start#main.py)
- local scope exists within functions
- global scope
- it not only applies to variables, it also applies to functions and basically anything else you name -> namespace

## Does Python Have Block Scope?
- There is no Block scope
- If we create a variable within a function, then it's only available within that function

## How to Modify a Global Variable
- way 1: `global` keyword
- way 2: `return` keyword

## Python Constants and Global Scope
- [end](https://replit.com/@appbrewery/day-12-end)
- useful when defining constants
- Global Constants are variables which you define and never change it
- naming convention of constant: UPPERCASE

## Project: The Number Guessing Game
- [Get ASCII text](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- [start](https://replit.com/@appbrewery/guess-the-number-start#main.py)
- [python tutor](https://pythontutor.com/visualize.html#mode=edit)
- [solution](https://replit.com/@appbrewery/guess-the-number-final#main.py)