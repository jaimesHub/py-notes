print(bool([])) # check falsy/truthy
print(bool(None))
print(bool(200))

# empty / falsy values
data: dict = {}
my_list: list = []
my_tuple: tuple = ()
empty_string: str = ''

# truthy values
users: dict = {1: 'Mario', 2: 'Luigi', 3: 'James'}
# users: dict = {}
# users: list = []
# users = None
if users:
    for k, v in users.items():
        print(k, v, sep=': ')
else:
    print('No data found...')

# Anything contains values be considered truthy values
# otherwise (None, False, 0, [], {}) they represent falsy values