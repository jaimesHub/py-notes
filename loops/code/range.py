for num in range(5, 10):
    print(num)

# 5, 6, 7, 8, 9

for num in range(10):
    print(num)

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for num in range(10):
    print("HELLO WORLD!")

# Adding optional step
for num in range(0, 102, 2):
    print(num)
# 0, 2, 4, 6, ..., 100

# This does not work
for num in range(10, 1):
    print(num)

# Fix this
for num in range(10, 1, -1):
    print(num)
# Same
count = 10
while count > 1:
    print(count)
    count -= 1