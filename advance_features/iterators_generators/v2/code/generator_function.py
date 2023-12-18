def squares(length):
    for n in range(length):
        yield n ** 2

for square in squares(5):
    print(square)

# defines a generator expression that returns square numbers of integers from 0 to 4
squares_2 = (n**2 for n in range(5)) # <generator object <genexpr> at 0x1041cf920>
# print(squares_2)

for square in squares_2:
    print(square)