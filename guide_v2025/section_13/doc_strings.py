"""
This is a docstring
"""

class User:
    """
    Base class for creating users.
    """
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def show_id(self) -> None:
        """
        Prints the user's ID.
        """
        print(self.user_id)

def user_exists(user: User, database: set[User]) -> bool:
    """
    sphinx style
    Check if a user is inside a database.

    :param user: User to check.
    :param database: the database to check inside.
    :return: bool
    """
    return user in database

def main() -> None:
    user: User = User(1234)
    user.show_id()

    bob: User = User(1)
    anna: User = User(2)

    database: set[User] = {bob, anna}

    if user_exists(bob, database):
        print('User exists in database.')
    else:
        print('User not found.')

    print(User.__doc__)
    print(user_exists.__doc__)

if __name__ == '__main__':
    main()