class Cat:
    def __init__(self, name):
        self.name = name
        self.say_hello = self.meow

    def meow(self):
        print(f"{self.name} meows!!!")


class Dog:
    def meow(self):
        print("12345")
class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")

    def meow(self):
        print("1111")

class Lion(Dog, Cougar):
    def roar(self):
        print(f"{self.name} roars!!!")


lion_ins = Lion("a")
lion_ins.say_hello()
        