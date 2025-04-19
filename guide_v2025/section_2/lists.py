my_list: list = [1, True, 'Text', [1,2,3]]
print(my_list)

people: list[str] = ['Bob', 'James', 'Tom']
print(people)

print(people[0])
print(people[2])

print('Original: ', people)

# Append
people.append('Jeremy')
print(people)

# Remove
people.remove('Jeremy')
print(people)

# Pop
people.pop()
print(people)

people[0] = 'Charlotte'
print(people)

people.insert(1, 'Timothy')
print(people)

# Clear
people.clear()
print(people)
