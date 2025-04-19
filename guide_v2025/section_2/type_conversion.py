txt_value: str = '100'
int_value: int = 50

# print(txt_value + int_value) # TypeError

print(int(txt_value) + int_value) # Option 1
print(txt_value + str(int_value)) # Option 2

print(5.5 + 1)
print(type(5.5 + 1))

# print(int('ten')) # ValueError
print(int('5'))