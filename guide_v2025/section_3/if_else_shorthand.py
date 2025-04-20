number: int = 0

if number > 0:
    result: str = 'Above 0'
else:
    result: str = '0 and Below 0'
print(result)

# boolean expression / shorthand
result: str = 'Above 0' if number > 0 else '0 and Below 0'
print(result)

# same
condition: bool = True
var: str = 'True' if condition else 'False'
print(var)

# same
if condition:
    var: str = 'True'
else:
    var: str = 'False'
print(var)
