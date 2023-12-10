from abc import ABC, abstractmethod

class Person:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"This person has name: {self.name}"

# This class violates the OCP
class PersonStorage:
    """This class has 2 methods
    save_to_database which saves data into database
    save_to_json which saves data into a json file
    Later, if you want to save the Person's object into XML file,
    you need to modify this class.
    It means that this class is not open for extension but modification.
    Hence, this class violates the Open-Closed Principle
    """
    def save_to_database(self, data: Person):
        print(f"Save the {data} to database")

    def save_to_json(self, data: Person):
        print(f"Save the {data} to a JSON file")

# Applying the OCP to refactoring code
# Open for extension but closed for modification
class PersonStorageFollowsOCP:
    @abstractmethod
    def save(self, data: Person):
        pass

class PersonDB(PersonStorageFollowsOCP):
    def save(self, data: Person):
        print(f"Save the {data} to database")

class PersonJSON(PersonStorageFollowsOCP):
    def save(self, data: Person):
        print(f"Save the {data} to a JSON file")

class PersonXML(PersonStorageFollowsOCP):
    def save(self, data: Person):
        print(f"Save the {data} to a XML file")
    
if __name__ == "__main__":
    # Violation of the OCP
    # person = Person("John Doe")
    # storage = PersonStorage()
    # storage.save_to_database(person)

    # Using OCP to refactor code
    jackson = Person("Jackson Blue")

    # originally, we save data into database
    # storage = PersonDB()

    # some beautiful day, we want to save data as a json file, 
    # we don't want to modify our class
    # storage = PersonJSON()

    # some day, we want to save data as XML data
    # we just add one more class
    storage = PersonXML()

    storage.save(jackson)