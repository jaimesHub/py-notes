# This UserBad class is not following the Single Responsibility Principle 
# as it has two responsibilities: 
# managing user properties and sending confirmation emails.
class UserBad:
    """
    This is an example of a class in Python that is NOT following the
    Single Responsibility Principle
    """
    def __init__(self, username, email_address) -> None:
        self.username = username
        self.email_address = email_address
        self.send_confirmation_email()

    def send_confirmation_email(self):
        print(f"Sending confirmation email to {self.email_address}")
