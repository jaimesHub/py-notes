class User:
    active_users = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        # each time we initailize an User instance
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logout"
    
    # Instance Methods
    def full_name(self):
        "self means instances of object"
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        "Joe likes candy"
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
    
    def say_hi():
        print("HELLO!")

print(User.active_users)

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 42)

print(User.active_users)

print(user2.logout())

print(User.active_users)

