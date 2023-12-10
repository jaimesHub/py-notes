from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def fly(self):
        print("Flying")

    def go(self):
        print("Running")

class Car(Movable):
    def go(self):
        print("Going")

if __name__ == "__main__":
    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()

    car = Car()
    car.go()

