# This is a loosely coupled example that follows the Dependency Inversion Principle 
# as the class UseCase depends on the abstract class Storage.
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self, data):
        pass

class MySQLStorage(Storage):
    def get(self):
        print("Get data from MySQL Database")
    
    def set(self, data):
        print(f"Set {data} into MySQL Database")

# To also save in a CSV file in addition to saving in the MySQL database, 
# we don’t need to change the UseCase class. 
# We just create the CSVFileStorage class and use it.
class CSVFileStorage(Storage):
    def get(self):
        print("Get data from CSV File")
    
    def set(self, data):
        print(f"Set {data} into CSV File")

class UseCase():
    def run(self, storage: Storage):
        storage.get()
        storage.set({"data": "Helloworld"})

if __name__ == "__main__":
    use_case = UseCase()
    use_case.run(MySQLStorage())
    use_case.run(CSVFileStorage())