num = 333
str(num)

def outer():
    animal = "Secretary Bird"
    def inner():
        print("INSIDE INNER FUNC: ", animal)
        def third():
            print("INSIDE THIRD NESTED FUNC: ", animal)
            str(num)
        third()
    inner()

outer()

# help(builtins)