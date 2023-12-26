animal = "Lemur"

print("OUTSIDE FUNCTION: ", animal)

def func():
    print("INSIDE FUNCTION: ", animal)

    def inner_func():
        print("INSIDE INNER FUNCTION: ", animal)

    inner_func()

func()