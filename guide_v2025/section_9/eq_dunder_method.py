# Comparing objects
from typing import Self

class Car:
    def __init__(self, brand: str, car_id: int, color: str) -> None:
        self.brand = brand
        self.car_id = car_id
        self.color = color

    def __eq__(self, other: Self) -> bool:
        # return self.car_id == other.car_id
        print('Current: ', self.__dict__)
        print('Other: ', other.__dict__)
        return self.__dict__ == other.__dict__ # this will check the contents of each class
def main() -> None:
    car1: Car = Car('BMW', 1, 'red')
    car2: Car = Car('BMW', 1, 'red')

    print(car1 == car2) # => False: why is that ?

    # because
    print(car1)
    print(car2)

    # solution: __eq__

if __name__ == '__main__':
    main()