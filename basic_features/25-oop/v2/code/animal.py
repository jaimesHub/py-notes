class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")

class Cat(Animal):
    def __init__(self, name, species, breed, toy) -> None:
        # Animal.__init__(self, name, species)
        super().__init__(name, species)
        # self.name = name
        # self.species = species
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Cat", "Scottish Fold", "String")
# print(blue)
# print(blue.name)
# print(blue.species)
# print(blue.breed)
# print(blue.toy)

blue.play()

