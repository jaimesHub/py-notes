# The example below violates the Liskov Substitution Principle 
# as the calculate Father class returns a value 
# and the method from SonBadExample class prints it.

class Father():
    """ Example of a base class
    """
    def add(self, first: float, second: float) -> float:
        """ Do a calculation
        """
        return first + second
    
class SonBadExample(Father):
    """ Example of a child class that violates the Liskov Substitution
        Principle
    """
    def add(self, first: float, second: float) -> None:
        """ Do a calculation
        """
        print(first + second)