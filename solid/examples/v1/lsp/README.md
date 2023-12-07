# The Liskov Substitution Principle (LSP)

## What
- The Liskov Substitution Principle states that a child class must be substitutable for its parent class.
    - We should be able to use the child class instead of the parent class `without` any problems.
    - This is valid for `base classes` that are `not` abstract classes as abstract classes `cannot` be instantiated.
## Example
- Problem: `ViolateLSP.py`
- Solution: `FollowLSP.py`