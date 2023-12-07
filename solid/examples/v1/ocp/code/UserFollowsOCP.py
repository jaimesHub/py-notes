# each of these has its own class and if we need additional responsibility, 
# we would create another class.

class User:
    def __init__(self, username, name) -> None:
        self.username = username
        self.name = name

class UserDatabse:
    def save(self, user: User):
        print(f"Saving {user} data into database")