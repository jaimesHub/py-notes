class User:
    def __init__(self, first, last, age):
        self.first = first # Instance Attributes
        self.last = last # Instance Attributes
        self.age = age # Instance Attributes
    
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


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 42)
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user2.full_name())
print(user1.likes("Ice Cream"))
print(user2.initials())
print(user1.is_senior())
print(user2.birthday())

# error when define method without self
# print(user2.say_hi())
