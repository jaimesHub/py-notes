class Dog:
    species = "canine"
    num_dogs = 0

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1

    @classmethod
    def register_stray(cls):
        # print(cls) # <class __main__.Dog>
        # cls() = Dog()
        return cls('coming soon', 'unknown', 'unknown')
    
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