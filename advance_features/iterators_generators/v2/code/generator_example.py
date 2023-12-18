def greeting():
    """it executes the code line by line from top to bottom."""
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

# When you call a generator function, it returns a generator object
# the `messenger` also is an iterator
messenger = greeting()
# print(messenger) # <generator object greeting at 0x102f1ca00>
# it is also an iterator

# To actually execute the body of the greeting() function
# you need to use the next() built-in function
result = next(messenger)
print(result)
'''
Hi!
1
'''
# it’s paused right at the first yield statement

# If you “call” the greeting() function again, 
# it’ll resume the execution from the last yield statement
result = next(messenger)
print(result)
'''
How are you?
2
'''

# And you can call it again
result = next(messenger)
print(result)
'''
Are you there?
3
'''

# However, if you execute the generator once more time, 
# it’ll raise the StopIteration exception because it’s an iterator
next(messenger)