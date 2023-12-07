# The example below doesn’t follow the Open-Closed Principle 
# as we would need to change the class if we wanted to include an additional feature 
# like a more exclusive option like private banking.
class InterestRateBadExample:
    """Classes with conditional logic"""
    def get_interest_rate(self, category):
        if category == 'standard':
            return 0.03
        elif category == 'premium':
            return 0.05