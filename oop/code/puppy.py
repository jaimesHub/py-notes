# define "class" 
    # with Class Name is Capitalized
        # define "def"
            # special "__init__" method automatically called whenever 'new Puppy is created'
                # self: refers to the "current" instance of Puppy, it must be the first parameter to init
                # other parameters

# instatiating
    # to create a Puppy instance, call Puppy() and provide a name
    # __init__  method runs first

# define
class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    # define method
    def bark(self):
        print(f"{self.name} says WOOF!")

    # def eat():
    #     print("NOM NOM!")

    def eat(self):
        print("NOM NOM!")

# instatiating
otter = Dog("otter", "Husky", 9999)

# otter
# type(otter)
# isinstance(otter, Dog)

# otter.name
# otter.breed
# otter.location
# otter.tricks

jules = Dog("Jules", "Corgi", 10003)

# jules.name
# jules.breed
# jules.location
# jules.tricks

tina = Dog('tina', 'mutt', 123)
tina.bark()

doggy = Dog("doggy", "dog", 113)
doggy.bark()

# error: eat() takes 0 positional arguments but 1 was given
# doggy.eat()