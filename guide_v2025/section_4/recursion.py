# def func() -> None:
#     print('Recursion')
#     func() # infinty loop
#
# func() # RecursionError

import time

def connect_to_internet(signal: bool, delay: int) -> None:
    if delay > 5:
        signal = True

    if signal:
        print('Connected!')
    else:
        print(f'Failed to connect! Tying again in: {delay}s...')
        time.sleep(delay)
        connect_to_internet(signal, delay + 2)

connect_to_internet(False, 0)