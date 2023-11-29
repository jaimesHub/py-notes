class Dog:
    species = "canine"
    num_dogs = 0

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1

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

# all instances of `Puppy` will have (share) the `same` value for `species`
elton = Dog('elton', 'australian shepherd', 9827)
print(elton.species)

meatloaf = Dog('meatloaf', 'pug', 124)
print(meatloaf.species)

print(Dog.species)
Dog.species = 'C.Lupus'
print(Dog.species)
print(elton.species)
print(meatloaf.species)