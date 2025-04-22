# def check_age(age: int) -> bool:
#     if age < 0:
#         raise ValueError('age cannot be negative')
#     elif age >= 21:
#         print('You are old enough')
#         return True
#     else:
#         print('You are not old enough')
#         return False
#
# check_age(30)
# check_age(10)
# check_age(-20)

raise Exception('This is a general exception.')

# https://docs.python.org/3.12/library/exceptions.html