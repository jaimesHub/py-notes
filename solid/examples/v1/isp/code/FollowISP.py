# Those classes from now on follow the Interface Segregation Principle
# Instead of having one abstract class for all employees, we divided them by
# roles and the child class uses multiple inheritance.
# If you don’t know what multiple inheritance is, the Chef class has multiple
# inheritance as it has two parent classes. Chef class inherits the lead method
# from the Leader class and the cook method from the Cook class.

from abc import ABC, abstractmethod

class Cook(ABC):
    """ An abstract class representing a cook (person who cooks)
    """
    @abstractmethod
    def cook(self):
        pass

class Leader(ABC):
    """ An abstract class representing a leader
    """
    @abstractmethod
    def lead(self):
        pass

class Coding(ABC):
    """ An abstract class representing a coding skill (person who codes)
    """
    @abstractmethod
    def write_code(self):
        pass

class Chef(Cook, Leader):
    def cook(self):
        print("I'm cooking")

    def lead(self):
        print("I'm leading in a Restaurant")

class Developer(Coding, Leader):
    def write_code(self):
        print("I'm coding")

    def lead(self):
        print("I'm leading in a Dev Team") 

# Alternatively, the method could be implemented directly on the child class
# without relating it to the parent class. The fly method of the Bird class
# below is an example of this approach.   
class Animal(ABC):
    """ An abstract class representing an animal
    """

    @abstractmethod
    def eat(self):
        """ Eat method
        """
        pass

class Bird(Animal):
    """ Bird Class
    """
    def eat(self):
        print("I am eating")

    def fly(self):
        """ The Fly method could be implemented directly on it
        without relating it to the parent class (Animal)
        """
        print("I am flying")