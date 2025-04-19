users: dict = {1: 'Bob', 2: 'Luigi'}
empty: dict = {}
print(users)
print(empty)

print(users[2])
# print(users[0])

weather: dict = {'time': '12:00', 'weather': {'morning': 'rain', 'evening': 'more rain'}}
print(weather)
print(weather['time'])
print(weather['weather'])
print(weather['weather']['morning'])

# users[3] = 'Mario'
# print(users)

# users[1] = 'James'
# print(users)

# users.pop(2)
# print(users)

del users[2]
print(users)

users.clear()
print(users)
