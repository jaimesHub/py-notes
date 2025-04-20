for i in range(3):
    print(f'Interation: {i}')
    # break # if error/not fully iterating then else does not execute
else:
    print('Success!') # if for loop iterates successfully


i: int = 3

while i > 0:
    i -= 1
    print('OK')
    # break
else:
    print('Success!')