# while True:
#     print('Hello')

# i: int = 5
# while i > 0:
#     print(f'Hello: {i}')
#     i -= 1

import time
connected: bool = True

while connected:
    print('Using internet...')
    time.sleep(5)
    connected = False
    print('Connection ended...')

# while True:
#     user_input: str = input('You: ')
#
#     if user_input == 'hello':
#         print('Bot: Hey there!')
#     else:
#         print('Bot: Yes, that is interesting.')