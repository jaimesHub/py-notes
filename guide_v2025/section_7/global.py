# var: int = 10
#
# # inner_var
#
# def func() -> None:
#     # var = 5
#     print(var)
#
#     # inner_var
#
#     def func2() -> None:
#         inner_var = 1
#         print(var)
#
#         def func3() -> None:
#             print(inner_var)
#
# # inner_var

number: int = 0

def change_number() -> None:
    global number
    number = 10

print(number)
change_number()
print(number)