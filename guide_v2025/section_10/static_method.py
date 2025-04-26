class Calculator:
    def __init__(self, version: int) -> None:
        self.version = version

    # def add(self, *numbers: float) -> float: # warning because it does not affect the class/not be affected by class
    #     return sum(numbers)

    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> int:
        return self.version

    # @staticmethod
    # def get_version() -> int:
    #     return 10

def main() -> None:
    calc: Calculator = Calculator(version=1)
    result: float = calc.add(1, 2, 3, 4, 5)
    print(result)

    other: float = Calculator.add(1, 2, 3, 4, 5)
    print(other)

if __name__ == '__main__':
    main()

# benefit ???