from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Aircraft(Vehicle):
    def fly(self):
        print("Flying")

    def go(self):
        print("Running")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise ValueError("Can not fly")

if __name__ == "__main__":
    aircarft = Aircraft()
    aircarft.fly()

    car = Car()
    car.go()