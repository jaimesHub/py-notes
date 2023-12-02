from collections import defaultdict

my_dict = defaultdict(lambda: 'Default Value')

print(my_dict)

my_dict['a'] = 42

print(my_dict['a'])
print(my_dict['b']) # b is not defined before