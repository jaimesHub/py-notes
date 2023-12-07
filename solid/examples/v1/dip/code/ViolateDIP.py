# Below is a tightly coupled example that violates the Dependency Inversion Principle 
# as the class MySQLStorageBadExample is called directly without using an abstraction.
class MySQLBadExample:
    def get(self):
        print("Get data from MySQL Database")
    
    def set(self, data):
        print(f"Saving {data} into MySQL Database")

class UseCaseBadExample:
    def run(self):
        bad_storage = MySQLBadExample()
        bad_storage.get()
        bad_storage.set({"data": "Helloworld"})

if __name__ == "__main__":
    use_case = UseCaseBadExample()
    use_case.run()