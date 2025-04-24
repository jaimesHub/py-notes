numbers: list[int] = [1, 2, 3, 4, 5, 6]

print(numbers[0:3]) # 3 is excluded
print(numbers[2:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[3:] + numbers[:3])
print(numbers[-1])
print(numbers[-2])
print(numbers[0:4:2])
print(numbers[0:4:-2])
print(numbers[4:0:-2])
print(numbers[::])

name: str = 'Mario'
print(name[0:4:2])

