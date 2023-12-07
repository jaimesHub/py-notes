# Open–Closed Principle (OCP)

## What

- OCP states that software entities should be `open` for `extension` but `closed` for `modification`.
    - It means that we should be able to add new functionality to the code without having to modify existing classes
- There are 3 cases when we should pay attention to not breaking the Open-Closed Principle

## When (3 cases of violation)

### Classes with conditional logic
- `Classes with conditional` logic that handle different cases aren’t open to extension because every time an additional option is added, the class needs to be modified.
- Problem: `InterestRateBadEx.py`
- Solution: `InterestRateFollowsOCP.py`

### Classes that violate the Single Responsibility Principle
- Classes that `violate` the `Single Responsibility Principle` also don't follow the Open/Closed Principle as we would need to change the class if we need to include another responsibility.
- Problem: `UserBad.py`
- Solution: `UserFollowsOCP.py`

### Classes that are tightly coupled
- Tight coupling of classes occurs in several situations. Some will require us to use `dependency inversion`, which we will discuss later.
- Problem: `TightCoupling.py`
- Solution: ?
        