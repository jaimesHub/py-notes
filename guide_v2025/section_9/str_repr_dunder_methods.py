# __repr__: representation
# __str__: string

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """Create for users / yourself to read easily"""
        return f'{self.name}: {self.age} years old'

    def __repr__(self) -> str:
        """Shows detail what dev wants to see/understand (Technical Docs)"""
        return f'Person(name={self.name}, age={self.age})'

def main() -> None:
    mario: Person = Person("Mario", 19)
    # print(mario) # => <__main__.Person object at 0x109d55d00> => define __str__
    print(mario) # => Mario: 19 years old

    # print(repr(mario)) # => <__main__.Person object at 0x1030fe120>
    print(repr(mario)) # => Person(name=Mario, age=19)

if __name__ == '__main__':
    main()