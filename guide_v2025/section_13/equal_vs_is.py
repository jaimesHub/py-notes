# a: int = 200
# b: int = 200
#
# print(a == b)
# print(a is b) # save memory

a: int = 1000
b: int = int('1000')

print(a == b)
print(a is b) # do not use `is` when you're trying to check for the value of an object or of a variable

print(f'{id(a)=}')
print(f'{id(b)=}')

var: int | None = None

if var is None: # correct
# if var == None: # wrong
    print('There is no var...')
else:
    print(f'var is {var}')

class Animal:
    ...

cat = Animal()
dog = Animal()

print(id(cat), id(dog))
print(cat is dog)
print(cat is cat)