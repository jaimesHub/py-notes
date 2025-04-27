elements: list[str] = ['A', 'B', 'C', 'D', 'E', 'F']
i: int = 0

for element in elements:
    i += 1
    print(f'{i}: {element}')

# using enumerate instead
enumeration: enumerate = enumerate(elements, start=1)
# print(enumeration) # display a memory address
# print(list(enumeration))

for i, element in enumeration:
    print(f'{i}: {element}')

# combine 2 examples

for i, element in enumerate(elements, start=1): # using start=... be much more performant approach
    print(f'{i}: {element}')