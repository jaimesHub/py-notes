import  sys

total: int = 0
while True:
    user_input = input('Enter a number: ')

    if user_input == '0':
        print('Total: ', total)
        sys.exit(0)

    total += int(user_input)

# Error: Input a string
# Error: Input a float