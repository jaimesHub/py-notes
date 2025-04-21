def greet(name: str): # parameters
    print(f"Hello, {name}!")

greet("Mario")
greet("James") # pass a value as an argument

# multiple parameters
def greet_with_parameters(name: str, language: str, default: str):
    if language == 'it':
        print(f"Ciao, {name}!")
    else:
        print(f"{default}, {name}!")

greet_with_parameters('Mario', 'it', 'Hello')
greet_with_parameters('Mario', 'asd', 'Hello')

# keyword arguments
greet_with_parameters(name='Mario', language='it', default='Hello')

# put them in any order with keyword arguments
greet_with_parameters(default='Hello', name='Mario', language='it')

# mix keyword arguments w normal arguments
# greet_with_parameters(default='Hello', 'Mario', language='it') # error
greet_with_parameters('Mario', default='Hello', language='it')

# default values
def greet_with_default_value(name: str, language: str, default: str = 'Hello'):
    if language == 'it':
        print(f"Ciao, {name}!")
    else:
        print(f"{default}, {name}!")
greet_with_default_value('Mario', language='it')
greet_with_default_value('Mario', language='asd', default='Hola')