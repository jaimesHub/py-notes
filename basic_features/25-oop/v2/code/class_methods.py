class User:
    active_users = 0

    # class methods, cls = class
    @classmethod
    def display_active_users(cls):
        # print(cls)
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

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

# example 1
# user1 = User("Joe", "Smith", 68)
# print(User.display_active_users())

# user2 = User("Blanca", "Lopez", 42)
# print(User.display_active_users())

# user1.display_active_users()
# print(User.display_active_users())

# exmaple 2
jack = User.from_string("Jack,Blue,29")
print(jack.first)
print(jack.full_name())
print(jack.birthday())


