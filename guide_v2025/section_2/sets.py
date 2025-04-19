elements: set = {99, True, 'Bob'}

print(elements) # random positions

# Add elements
elements.add('James')
print(elements)

# Remove elements
elements.remove('Bob')
print(elements)

# Pop
elements.pop() # random element
print(elements)

# Clear
elements.clear()
print(elements)

# Can not use this syntax
print(elements[0]) # TypeError

# empty_set: set = tuple()
# empty_set: tuple = tuple()
# empty_set: set = set()
empty_set: set = {}
print(empty_set)