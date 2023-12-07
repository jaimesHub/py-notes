class UserBadExample:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def get_user_bad_example(user_bad_example: UserBadExample):
    """The function get_user_bad_example is tightly coupled to the UserBadExample class 
    as we would need to change the function if we need to change the UserBadExample class. 
    That also violates the Open/Close Principle."""
    return {
        "name": user_bad_example.name,
        "age": user_bad_example.age
    }