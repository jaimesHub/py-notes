from abc import ABC, abstractmethod

class EmployeeBadExample(ABC):
    """The abstract class EmployeeBadExample doesn't follow the Interface Segregation Principle 
    as it has methods that aren't used by its children.
    """
    @abstractmethod
    def write_code(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def lead(self):
        pass

class ChefBadExample(EmployeeBadExample):
    """the write_code method isn’t used by the ChefBadExample class"""
    def write_code(self):
        raise NotImplementedError("Chef does not write code!")
    
    def cook(self):
        print("I'm cooking!")

    def lead(self):
        print("I'm leading")