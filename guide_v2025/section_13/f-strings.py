# Help for debugging

var: int = 10

def add(a: int, b: int) -> int:
    return a + b

print(f'{var=}')
print(f'var={var}')

print(f'{add(5,10)=}')

big_number: float = 123456789
# big_number: float = 123_45_6789
print(f'{big_number:,}')
print(f'{big_number:_}')

fraction: float = 1234.5678
print(f'{fraction:.2f}')
print(f'{fraction:,.2f}')

percent: float = 0.555555
print(f'{percent:.2%}')
print(f'{percent:.0%}')
percent: float = 555555.555555
print(f'{percent:_.3%}')

var: str = 'BOB'
print(f'{var:10}: Hello')
print(f'{var:>10}: Hello')
print(f'{var:<10}: Hello')
print(f'{var:^10}: Hello')

print(f'{var:*>10}: Hello')
print(f'{var:*<10}: Hello')
print(f'{var:%^10}: Hello')

numbers: list[int] = [1, 100, 1_000, 10_000]
for number in numbers:
    print(f'{number:_>5}: {number}')

path: str = '\\Users\\fer\\Documents\\'
print(path)

# or
user: str = 'Fer'
# path: str = r'\Users\user\Documents'
path: str = fr'\Users\{user}\Documents'
# path: str = rf'\Users\{user}\Documents'
print(path)


