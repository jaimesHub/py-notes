# def count_stuff(*args):
#     # print(args)
#     print(f"You passed me {len(args)} arguments")

# def count_stuff(*things):
#     # print(args)
#     print(f"You passed me {len(things)} arguments")

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def silly(first, second, *others):
    print(f"first is {first}")
    print(f"second is {second}")
    print(f"others: {others}")

# silly(1) # error because "second" is required
# silly(1,2) # ok
# silly(1,2,3,4,5,6) # ok

# nums = [1,2,3,4,5,6,7]
# sum(nums) # type error
# sum(*nums) # ok