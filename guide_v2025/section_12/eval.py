result: int = eval('1 + 10 + 100')
print(result)

x: int = 5
y: int = 10
print(eval('x + y'))

while True:
    user_input: str = input('Enter math: ')
    print(eval(user_input))