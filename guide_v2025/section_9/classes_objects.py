# class as a blueprint
class Car:
    # define initializer: starting some information
    def __init__(self, brand: str, wheels: int) -> None:
        self.brand = brand
        self.wheels = wheels

    # define functionalities
    def turn_on(self) -> None:
        print(f'{self.brand} turned on')

    def turn_off(self) -> None:
        print(f'{self.brand} turned off')

    def drive(self, km: float) -> None:
        print(f'{self.brand} driving {km} km/h')

    def describe(self) -> None:
        print(f'{self.brand} is a car with {self.wheels} wheels')

# => Now we have a blueprint

def main() -> None:
    # Object
    bmw: Car = Car('BMW', 4)
    bmw.turn_on()
    bmw.drive(10)
    bmw.turn_off()
    bmw.describe()

    # benefit of using classes
    # Object
    volvo: Car = Car('Volvo', 6)
    volvo.turn_on()
    volvo.drive(30)
    volvo.turn_off()
    volvo.describe()

if __name__ == '__main__':
    main()
