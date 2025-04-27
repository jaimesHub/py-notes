numbers: list[int] = [1, 2, 3, 4, 5]

my_range: range = range(1, 6) # 6 is excluded
print(my_range) # range object
print(list(my_range))

my_range_2: range = range(5)
print(my_range_2)
print(list(my_range_2))

my_range_3: range = range(0, 10, 2)
print(my_range_3)
print(list(my_range_3))

my_range_4: range = range(-5, 0)
print(my_range_4)
print(list(my_range_4))

my_range_5: range = range(0, -5) # empty list
print(my_range_5)
print(list(my_range_5))

my_range_6: range = range(0, -5, -1)
print(my_range_6)
print(list(my_range_6))

# ranges are iterable
for i in range(3):
    print(i)