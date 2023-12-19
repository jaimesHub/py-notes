def plus_one(number):
    def add_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))
# calling plus_one(number = 4)
# result = add_one(number = 4)
# result = 5
# return 5