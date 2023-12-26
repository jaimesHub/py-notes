def laugh(strength = 2):
    print("HA!" * strength)

# laugh(10) # output: HA!HA!HA!HA!HA!HA!HA!HA!HA!HA!
# laugh() # output: HA!HA!

def slugify(phrase, sep="-"):
    return phrase.lower().strip().replace(" ", sep)

# print(slugify("hello world chicken face"))
# print(slugify("hello world chicken face", "_"))

def divide(x = 1, y = 4):
    return x / y

print(divide(8)) # output: 2.0

# Ordering Default Parameters
# def greet(msg, person):
#     print(f"{msg}, {person}!")

# greet("hello", "jack")
# Error: Non-default argument follows default argument
# def greet(msg="Hi", person):
#     print(f"{msg}, {person}!")
# greet("jack")
# Solution
# def greet(person, msg="Hi"):
#     print(f"{msg}, {person}!")
# greet("jack")

def greet(person="stranger", msg="Hi"):
    print(f"{msg}, {person}!")
greet()
greet("Bye") # output: Hi, Bye