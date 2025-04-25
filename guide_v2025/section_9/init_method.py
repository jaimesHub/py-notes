# Initializer: What & How

class Connection:
    def __init__(self, connection_type: str, cost: float) -> None: # self refers to the current instance of this class
        """Take care of the code that initializes the object (class)
        """
        print(f'{connection_type} connection established! (Cost: {cost}/h)')
        self.connection_type = connection_type
        self.cost = cost

    def close_connection(self) -> None:
        print(f'{self.connection_type} connection closed.')

def main() -> None:
    # internet is an instance of a Connection
    internet: Connection = Connection('internet', 2)
    satellite: Connection = Connection('satellite', 20)

    internet.close_connection()
    satellite.close_connection()

if __name__ == '__main__':
    main()
