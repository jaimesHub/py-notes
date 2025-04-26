from abc import ABC, abstractmethod

class Appliance(ABC):
    def __init__(self, brand: str, version_no: int) -> None:
        self.brand = brand
        self.version_no = version_no
        self.is_turn_on: bool = False

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        ...

class Lamp(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    # Remove warning: Class Lamp must implement all abstract methods

    def turn_on(self) -> None:
        if self.is_turn_on:
            print(f'{self.brand} is already turned on!')
        else:
            self.is_turn_on = True
            print(f'{self.brand} is turned on!')

    def turn_off(self) -> None:
        if self.is_turn_on:
            self.is_turn_on = False
            print(f'{self.brand} is turned off!')
        else:
            print(f'{self.brand} is already turned off!')

class Oven(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    # def turn_off(self) -> None:
    #     ...
    #
    # def turn_on(self) -> None:
    #     ...

    def turn_off(self) -> None:
        # good habit
        raise NotImplementedError('Need to implement turn_off()')

    def turn_on(self) -> None:
        # good habit
        raise NotImplementedError('Need to implement turn_on()')

def main() -> None:
    lamp: Lamp = Lamp('Z-Lite', 1)

    lamp.turn_off()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()

    # oven: Oven = Oven('Bosch', 2) # TypeError

    oven: Oven = Oven('Bosch', 2)
    oven.turn_off()
    oven.turn_on()


if __name__ == '__main__':
    main()

