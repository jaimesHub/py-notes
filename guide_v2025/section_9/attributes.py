# Attributes (class & instance)
class Car:
    SPEED_LIMIT_KM: float = 140 # class attribute

    def __init__(self, brand: str) -> None:
        self.brand = brand # instance attribute

    def drive(self, *, speed: float) -> None:
        if speed > self.SPEED_LIMIT_KM:
            print(f'Limiter activated: Driving at {self.SPEED_LIMIT_KM} km/h')
        else:
            print(f'Driving at {speed} km/h')

class Animal:
    # tricks: list[str] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks: list[str] = []


    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)

def main():
    # toyota = Car('Toyota')
    # bmw = Car('BMW')
    # toyota.drive(speed=200)
    # bmw.drive(speed=210)
    #
    # Car.SPEED_LIMIT_KM = 99
    # # toyota.SPEED_LIMIT_KM = 99
    #
    # toyota.drive(speed=200)
    # bmw.drive(speed=210)

    cat: Animal = Animal('Helios')
    dog: Animal = Animal('Boomer')

    cat.teach_trick('Wash dishes')
    dog.teach_trick('Get a job')

    print(cat.tricks)
    # print(dog.tricks)

    dog.teach_trick('Do finances')
    dog.teach_trick('Invest in stocks')
    print(dog.tricks)

    # because we defined class attribute (tricks) => all instances share this list => solution: move to instance attribute

if __name__ == '__main__':
    main()