age: int = 20

if age >= 21:
    print('You may enter the club!')
else:
    print('You are not allowed in...')

weather: str = 'cloudy'

if weather == 'clear':
    print('It is a nice day!')
elif weather == 'cloudy':
    print('The weather could be better...')
elif weather == 'rainy':
    print('What an awful day!')
else:
    print('Unknown weather...')

# order is matter
age: int = 100
if age > 12:
    print('Teenager') # return here when age = 19, ignore the rest
elif age >= 18:
    print('Young adult')
elif age >= 12:
    print('Adult')
else:
    print('Unknown age...')

# order is matter
age: int = 100
if age >= 21:
    print('You are an adult.')
elif age >= 18:
    print('You are a young adult.')
elif age > 12:
    print('You are a teenager.')
else:
    print('Unknown age...')