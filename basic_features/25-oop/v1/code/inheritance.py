class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows!!!")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")

class Lion(Cat):
    def roar(self):
        print(f"{self.name} roars!!!")
        