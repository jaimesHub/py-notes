numbers: list[int] = [1, 10, 5, 3]
sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers) # asc by default

people: list[str] = ['Mario', 'James', 'Anna', 'anna', 'Tom']
# sorted_names: list[str] = sorted(people) # sorted by its ascii value
# sorted_names: list[str] = sorted(people, reverse=True)
sorted_names: list[str] = sorted(people, key=lambda x: len(x)) # key: how we want to sort
print(sorted_names)

class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name}={self.weight}kg'

cat: Animal = Animal('cat', 10)
dog: Animal = Animal('dog', 3.0)
kangaroo: Animal = Animal('kangaroo', 50.0)

sorted_animals: list[Animal] = sorted([cat, dog, kangaroo], key=lambda animal: animal.weight)
print(sorted_animals)