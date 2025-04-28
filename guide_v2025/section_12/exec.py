code: str = """
x: int = 10
y: int = 20

print(x + y)
print('Hello, world!')

for i in range(3):
    print(i)
"""

exec(code)

while True:
    user_input: str = input('Command: ')
    exec(user_input)

# only run code that you trust, do not use online
# !!! always use exec & eval with caution