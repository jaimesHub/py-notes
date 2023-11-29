class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f"{self.name} says WOOF!")

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
    
    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick}")

elton = Dog('elton', 'australian shepherd', 9827)

elton.learn_trick('sit')
elton.learn_trick('down')
# elton.learn_trick('down')

elton.perform_trick('sit')
elton.perform_trick('stay')

meatloaf = Dog('meatloaf', 'pug', 124)

meatloaf.learn_trick('spin')
meatloaf.learn_trick('down')

meatloaf.perform_trick('down')
meatloaf.perform_trick('stay')

# problem: change `tricks` without learn_trick method
meatloaf.tricks.append('stay')
# problem: change attributes directly
meatloaf.breed = 'pug mix'
