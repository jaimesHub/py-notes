print(1, 2, True, ['a', 'b', 'c']) # default they will be interpreted as arguments
print('A', 'B', 'C', sep='-', end='.\n') # custom separator (sep='...')
print('Bob') # by default, end='\n' from the previous code
print('Sam')

# Unpacking arguments
people: list[str] = ['Mario', 'James', 'Hannah']
print(people)

# print the elements with a separator and with an end => using asterisk(*)
print(*people, sep=', ', end='.') # unpack them into arguments