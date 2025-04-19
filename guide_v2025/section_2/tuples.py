items: tuple = 1, True, 'Text'
print(type(items))

# items: tuple = (1)

# coordinates: tuple = 1.5, 2.5, 3.5
# coordinates[0] = 10 # TypeError
# print(coordinates)

new_tuple: tuple = ()
print(type(new_tuple))

coordinates: tuple[float, float] = 1.5, 2.5
print(coordinates)