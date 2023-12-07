# On the other hand, the class below doesn't do polymorphism 
#but creates another method which follows the Liskov Substitution Principle.

class Father():
    """ Example of a base class
    """
    def add(self, first: float, second: float) -> float:
        """ Do a calculation
        """
        return first + second

class Son(Father):
    """ Example of a child class that follows the Liskov Substitution Principle
    """
    def print_addition(self, first: float, second: float) -> None:
        """ Do a calculation
        """
        print(self.add(first, second))