class User:
    def __init__(self, first, last, age):
        print("A NEW USER HAS BEEN MADE!")
        self.first = first
        self.last = last
        self.age = age
    pass

# we're instantiating a new user instance, which is a user object
user1 = User("Joe", "Smith", 68)
# print(user1.first)
# print(user1)
# print(type(user1))

# we can create other individual users.
# they are look the same but they are not same
user2 = User("Blanca", "Lopez", 42)
# print(user2.first)

# user3 = User()
# user3 = User()
# user3 = User()
