class Pet():

    # Class attribute: a list of permitted species
    allowed = ("cat", "dog", "bird", "lizard", "rodent")

    def __init__(self, kind, name):

        if kind not in Pet.allowed:
            raise ValueError(f"You can't have a {kind} as a pet here!")

        self.kind = kind
        self.name = name

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet here!")
        self.kind = species

fluffy = Pet("cat", "Fluffy")

print(fluffy.allowed)
# ("cat", "dog", "bird", "lizard", "rodent")

fluffy.set_species("rat")

fluffy.allowed = ["tiger", "bear"]
print(fluffy.allowed)
print(Pet.allowed)

Bro = Pet("bear", "Bro")
# ValueError: You can't have a bear as a pet here!