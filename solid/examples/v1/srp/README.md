# Single Responsibility Principle (SRP)

## What
- SRP states that: “A class should have one and only one reason to change, meaning that a class should have only one job”.

## Problem
- `UserBad.py`
- a `UserBad` class `should not` have the `responsibility` to `send` emails to them and `managing` user properties.

## Solution
- we separated the responsibilities, each responsibility in your respective class.
- each of these has its own class (User, Email)
- `User_SRP.py`