numbers: list[int] = list(range(21))
print(numbers)

def is_even(num: int) -> bool:
    return num % 2 == 0

even_numbers: filter = filter(is_even, numbers)
print(even_numbers) # filter object
print(list(even_numbers))

# using lambda
even_numbers_2: filter = filter(lambda num: num % 2 == 0, numbers)
print(even_numbers_2)
print(list(even_numbers_2))

people: list[str] = ['Anna', 'Bob', 'Betty', 'James', 'John']
long_names: filter = filter(lambda name: len(name) > 4, people)
print(list(long_names))

# or
ln: list[str] = [name for name in people if len(name) > 4]
print(ln)