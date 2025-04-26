class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    def drink(self):
        print(f"{self.name} is drinking.")

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bark(self) -> None:
        print(f"{self.name} is barking.")

    def routine(self) -> None:
        self.eat()
        self.drink()
        self.bark()

class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def meow(self) -> None:
        print(f"{self.name} is meowing.")

def main() -> None:
    dog = Dog("Boomerang")
    cat = Cat("Snowball")

    dog.bark()
    cat.meow()

    cat.eat()
    dog.eat()

if __name__ == '__main__':
    main()