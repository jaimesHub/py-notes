numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def double(number: int) -> int:
    return number * 2

doubled: map = map(double, numbers)
print(doubled)
print(list(doubled))

# or
doubled_2: map = map(lambda n: n * 2, numbers)
print(doubled_2)
print(list(doubled_2))

# or
doubled_3: list[int] = [double(number) for number in numbers] # number * 2
print(doubled_3)

numbers: list[int] = [1, 2, 3, 4, 5]
letters: list[str] = ["a", "b", "c"]

def combine_elements(number: int, letter: str) -> tuple[int, str]:
    return number, letter

combined: map = map(combine_elements, numbers, letters)
print(list(combined))

combined_2: map = map(lambda number, letter: (number, letter), numbers, letters)
print(list(combined_2))