numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[2:4])

text: str = "Hello World"
print(text)

first_three: slice = slice(0, 3)
print(first_three)
print(text[first_three])

reverse_slice: slice = slice(None, None, -1)
print(text[reverse_slice])

step_two: slice = slice(None, None, 2)
print(text[step_two])