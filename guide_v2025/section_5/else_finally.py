user_input: str = '10'
# user_input: str = 'abc'

try:
    result: float = 1 / float(user_input)
    print(f'1 / {user_input} = {result}')
except ValueError as e:
    print(f'You can not use "{user_input}" as a value.')
except ZeroDivisionError as e:
    print(f'Don\'t be silly, you can not divide by zero.')
else: # rarely see, hard to read, used by inexperience devs
    print('Success! There were no exceptions encountered.')
finally:
    print('FINALLY: I am always executed!')