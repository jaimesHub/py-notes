animal = "Nudibranch"

def outer():
    animal = "Echidna"
    def inner():
        print("FROM INNER FUNC: ", animal)
        # str = "HELLO WORLD!"
        print(str)
    print("FROM OUTER FUNC: ", animal)
    # print(animal)
    inner()

print("OUTSIDE OF FUNCTIONS: ", animal)
outer()

# output
# OUTSIDE OF FUNCTIONS: Nudibranch
# FROM OUTER FUNC: Echidna
# FROM OUTER FUNC: Echidna
# HELLO WORLD! 
# <str class>