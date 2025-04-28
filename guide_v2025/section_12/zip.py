numbers: list[int] = [1, 2, 3, 4]
letter: list[str] = ['a', 'b', 'c', 'd']
symbol: list[str] = ['!', '&', '$']

# zip list of same lengths
zipped: zip = zip(numbers, letter)
# print(zipped)
# print(list(zipped))

for n, l in zipped:
    print(n, l, sep=': ')

# zip list of different lengths
zipped_2: zip = zip(numbers, symbol)
print(list(zipped_2))
zipped_3: zip = zip(numbers, symbol, letter, strict=True)
print(list(zipped_3)) # ValueError