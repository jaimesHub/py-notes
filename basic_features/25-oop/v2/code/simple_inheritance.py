class Animal:
    def make_sound(self, sound):
        print(sound)

    cool = True

class Cat(Animal):
    pass

gandalf = Cat()
gandalf.make_sound("meow")  # meow
# print(gandalf.cool)  # True

print(isinstance(gandalf, Cat))
print(isinstance(gandalf, Animal))
print(isinstance(gandalf, object))
