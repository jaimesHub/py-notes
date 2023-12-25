year = input("what year were you born in? ")

if not year.isnumeric():
    year = input("It's not a number! Please try again! what year were you born in? ")
    
year = int(year)

print(f"you were born {2023 - year} years ago")