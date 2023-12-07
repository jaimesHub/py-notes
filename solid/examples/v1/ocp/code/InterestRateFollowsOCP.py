# Below is a possible solution where each category now has a different class. 
# And if we included another category, we would add an additional class.
from abc import ABC, abstractmethod

class InterestRate(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

class StandardInterestRate(InterestRate):
    def get_interest_rate(self):
        return 0.03
    
class PremiumInterestRate(InterestRate):
    def get_interest_rate(self):
        return 0.05