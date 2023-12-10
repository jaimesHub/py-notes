from abc import ABC, abstractmethod

class Database(ABC):
    """Define a database interface"""
    @abstractmethod
    def store_data(self, data: any):
        pass

class RemoteDatabase(ABC):
    """Define a remote database interface"""
    @abstractmethod
    def connect(self, uri: str):
        pass

class MySQLDatabase(Database, RemoteDatabase):
    def connect(self, uri: str):
        print("Connecting to MySQL Database...")
    
    def store_data(self, data: any):
        print("Using MySQL storing data...")
    
class InMemoryDatabase(Database):
    def store_data(self, data: any):
        print("Using In Memory storgin data...")
    
class App:
    def __init__(self, database: Database) -> None:
        self._database = database

    def save_settings(self):
        self._database.store_data('Some data')

if __name__ == "__main__":
    my_database_instance = MySQLDatabase()
    # my_database_instance = InMemoryDatabase()
    my_database_instance.connect('my-url')
    
    my_app = App(my_database_instance)
    my_app.save_settings()