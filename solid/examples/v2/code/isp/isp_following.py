from abc import ABC, abstractmethod

class Database(ABC):
    """Define an interface"""
    @abstractmethod
    def storeData(self, data: any):
        pass

class RemoteDatabase(ABC):
    """Define an interface"""
    @abstractmethod
    def connect(self, uri: str):
        pass

class SQLDatabase(Database, RemoteDatabase):
    def connect(self, uri: str):
        print("Connecting...")
    
    def storeData(self, data: any):
        print("Storing data...")

class InMemoryDatabase(Database):
    def storeData(self, data: any):
        return super().storeData(data)
    