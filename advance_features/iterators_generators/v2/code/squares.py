class Squares:
    """The following example defines an iterator that returns a square number of an integer."""
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2

        self.current += 1

        if self.current > self.length:
            raise StopIteration

        return result
    
length = 5
square = Squares(length) # same
for s in square:
    print(s)

# rewrites the Squares iterator as a generator function
# same but it’s much shorter and more expressive.
def squares(length):
    for n in range(length):
        yield n ** 2

length = 5
square = squares(length)
for s in square:
    print(s)