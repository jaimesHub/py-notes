class Fruit:
    def __init__(self, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def eat(self) -> None:
        print(f'Eating {self.grams}g of {self.name}')

def main() -> None:
    apple: Fruit = Fruit('Apple', 25) # apple instance => self -> apple, attributes associate with objects, not classes
    print(apple.name)
    apple.eat()
    banana: Fruit = Fruit('Banana', 10) # class (Fruit) shares information, while the object wants to have its own information
    print(banana.name)
    banana.eat()

    # self is a naming convention => can use `this` or anything

if __name__ == '__main__':
    main()