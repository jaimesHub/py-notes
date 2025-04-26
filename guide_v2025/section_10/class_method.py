from typing import Self

class Car:
    # class attribute
    LIMITER: int = 200 # we do not want our car has over 200 km/h

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    # def change_limiter(self, new_limit: int) -> None:
    #     self.LIMITER = new_limit # this refers to the instance, not the Car class

    @classmethod
    def change_limiter(cls, new_limit: int) -> None: # cls refers to Class (Car)
        cls.LIMITER = new_limit

    def display_info(self) -> None:
        print(f'{self.brand} (max={self.max_speed}, limiter={self.LIMITER})')

    # factory method
    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        """
        Factory method that helps us to create new instances with custom setter
        """
        lowered: str = brand.lower()
        max_speed: int = 200

        if lowered == 'toyota':
            max_speed = 270
        elif lowered == 'bmw':
            max_speed = 290
        elif lowered == 'volvo':
            max_speed = 300

        return cls(brand, max_speed)

def main() -> None:
    bmw = Car('BMW', 240)
    toyota = Car('Toyota', 190)

    bmw.display_info()
    toyota.display_info()

    # Car.change_limiter(100)
    # toyota.change_limiter(150) # => class method affects all of instances
    toyota.LIMITER = 500 # only for toyota instance

    # toyota.fuel = 5 # it does not init in __init__
    # print(toyota.fuel)

    bmw.display_info()
    toyota.display_info()

    volvo: Car = Car.autogenerate_max_speed('volvo')
    volvo.display_info()

    some_car: Car = Car.autogenerate_max_speed('Ferrari')
    some_car.display_info()


if __name__ == '__main__':
    main()