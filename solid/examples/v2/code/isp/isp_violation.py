from abc import ABC, abstractmethod

class Database(ABC):
    """Define an interface"""
    @abstractmethod
    def connect(self, uri: str):
        pass

    @abstractmethod
    def storeData(self, data: any):
        pass

class SQLDatabase(Database):
    def connect(self, uri: str):
        print("Connecting...")
    
    def storeData(self, data: any):
        print("Storing data...")

class InMemoryDatabase(Database):
    def connect(self, uri: str):
        return super().connect(uri)
    
    def storeData(self, data: any):
        return super().storeData(data)
    
'''
Problem: it might make sense to have a stored data method
because no matter if we are storing data in a SQLDatabase or in-memory, we want to be able to store data
but connect, that does not neccessarily make sense here.
Because when use InMemoryDatabase we can not connect anywhere -> having wrong interface (Database)
'''