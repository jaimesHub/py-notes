def get_length(text: str) -> int: # return type via type annotations
    print(f'Getting the length of {text}')
    return len(text)

name: str = 'Mario'
length: int = get_length(name)
print(length)
# print(get_length(name))
# should use type annotation

def make_upper(text: str) -> str:
    return text.upper()

print(make_upper('Hello'))

# Connects to the internet & return nothing
def connect_to_internet() -> None:
    print('Connecting to internet...')
    # return None # under the hood

var: str = connect_to_internet()
print(var)