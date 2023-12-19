def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"My arguments are: {arg1}, {arg2}")
        print(1)
        # function(arg1, arg2)
        print("Validate input")
        print(2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print(f"Cities I love are {city_one} and {city_two}")

cities("Hanoi", "HCM")