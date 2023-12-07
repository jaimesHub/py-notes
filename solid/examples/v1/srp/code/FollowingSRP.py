# Here we separated the responsibilities, each responsibility in your
# respective class. So, this example follows the Single Responsibility
# Principle. Before, we had two reasons to change the UserBad class, changing
# user properties and changing how the email is sent. Now, each of these has
# its own class.
class User:
    """ This class is an example of the Single Responsibility Principle in Python
    """
    def __init__(self, username, email_address) -> None:
        self.username = username
        self.email_address = email_address
        self.email = Email(self.email_address)
        self.email.send_confirmation_email()

class Email:
    """ This class is an example of the Single Responsibility Principle in Python
    """
    def _init_(self, email_address):
        self.email_address = email_address

    def send_confirmation_email(self):
        """ This method would send confirmation email
        """
        print(f"Sending confirmation email to {self.email_address}")