class Human:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age
    
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def rage(self):
        return self._age
    
    @rage.setter
    def rage(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")
        
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

jane = Human("Jane", "Goodall", 50)
# print(jane._age)

# then we cause problems potentially by setting this
# jane.age = -100 # fix on _init__

# print(jane.get_age())
# jane.set_age(10)
# print(jane.get_age())

# this is where property comes in
print(jane.rage)
jane.age = 33
print(jane.age)
print(jane.full_name)
jane.full_name = "Steve Woz"
print(jane.__dict__)

