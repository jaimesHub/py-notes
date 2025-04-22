# try:
#     result: float = 10 / 0
#     print(result)
# except Exception as e: # bad practice, cover too many cases
#     print(f'Error: {e}')
#
# print("even error occurs, we still can run this command!")

###

# while True:
#     try:
#         user_input = int(input('Enter a number: '))
#         print(f'10 / {user_input} = {10 / float(user_input)}')
#     except ZeroDivisionError as e:
#         print('You cannot divide by zero')
#     except ValueError as e:
#         print('Please enter a valid number')
#     except Exception as e:
#         print(f'Something else went wrong: {e}')

###

import  sys
total: float = 0
while True:
    user_input = input('Enter a number: ')

    if user_input == '0':
        print(f'Total: {total}')
        sys.exit(0)

    try:
        total += float(user_input)
    except ValueError as e:
        print('Please enter a valid number')
    except KeyboardInterrupt as e:
        print(f'Goodbye: {e}')