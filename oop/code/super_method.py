class Cat:
    def __init__(self, name):
        self.name = name
        print("INSIDE CAT INIT")

    def meow(self):
        print(f"{self.name} meows!!!")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")

class Lion(Cat):
    def __init__(self, name, pride_name):
        print("INDIE LION INIT")
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars!!!")