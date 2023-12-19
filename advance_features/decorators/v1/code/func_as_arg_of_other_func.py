def plus_one(number):
    return number + 1

def function_call(func):
    number_to_add = 5
    return func(number_to_add)

print(function_call(plus_one))

# how it works?
# line 8: call function_call() with param plus_one()
# inside function_call(), pass number_to_add = 5 into plus_one(number = 5)
# inside plus_one(number=5), return 6
# inside function_call(), return 6
# output: 6