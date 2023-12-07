# This UserBad class is not following the Open/Closed Principle 
# because if we need to add a responsibility, we would have to modify the class. 
# For example, if we add the feature of sending email like the example shown in the SRP example, 
# we need to modify the UserBad class.
class UserBad:
    """we had two reasons to change the UserBad class, 
    changing user properties and saving to the database."""
    def __init__(self, username, name) -> None:
        self.username = username
        self.name = name

    def save(self):
        print("Saving data into database")