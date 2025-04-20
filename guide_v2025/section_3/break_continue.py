# number: int = 5
#
# while number > 0:
#     number -= 1
#
#     if number == 2:
#         # print('Break at 2')
#         # break # this time to exit the loop
#         print('Skipping 2')
#         continue # move back to the top while
#
#     print(number)
#
# print('Done!')
#

total: int = 0

print('Welcome to Calc+! Add positive numbers, or insert "0" to exit.')
while True:
    user_input = int(input('Enter a number: '))

    if user_input < 0:
        print('Enter a positive number.')
        continue

    if user_input == 0:
        print(f'Total: {total}')
        break

    total += user_input