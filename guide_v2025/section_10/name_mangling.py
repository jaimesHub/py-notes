class Car:
    # __YEAR: int = 2000
    _YEAR: int = 2000


    def __init__(self, brand: str, fuel_type: str) -> None:
        self.__brand = brand
        self.__fuel_type = fuel_type
        self.__var: str = 'red'

        # self.var: str = 'red'

    def driving(self) -> None:
        print(f'Driving: {self.__brand}')

    def __get_description(self) -> None:
        print(f'{self.__brand}: {self.__fuel_type}')

    def display_color(self) -> None:
        self.__get_description()
        # print(f'{self.__brand} is {self.var.capitalize()}')
        print(f'{self.__brand} is {self.__var.capitalize()}')


class Toyota(Car):
    def __init__(self, fuel_type: str) -> None:
        super().__init__('Toyota', fuel_type)
        self.var = 100

    def get_year(self):
        # return self.__YEAR # error
        return self._YEAR

def main() -> None:
    car: Car = Car('BMW', 'Electronic')
    car.driving()

    # print(car.__get_description()) # AttributeError

    print(car._Car__brand)
    car._Car__get_description()

    toyota: Toyota = Toyota('Electronic')
    toyota.display_color()

if __name__ == '__main__':
    main()