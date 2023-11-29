# def display_info(person, status="single", *args):
#     print(f"person is: {person}")
#     print(f"status is: {status}")
#     print(f"args is: {args}")

# display_info("jack")
# display_info("jack", "double")
# display_info("jack", "double", 1,2,3,4)

####################################################

# def display_info(person, *args, status="single"):
#     print(f"person is: {person}")
#     print(f"status is: {status}")
#     print(f"args is: {args}")

# display_info("james", "purple", 4, 5, 6, 7, status="married")
# display_info("james", "purple", 4, 5, 6, 7, "married")

####################################################

def display_info(person, *args, status="single", **kwargs):
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"args is: {args}")
    print(f"kwargs is: {kwargs}")

display_info("james", 4,5,6,7,8, status="married", age=87, mood="happy")

####################################################

# error
# def display_info(status="single", person):
#     print(f"person is: {person}")
#     print(f"status is: {status}")