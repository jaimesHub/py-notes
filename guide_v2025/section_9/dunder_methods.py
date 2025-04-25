# dunder methods / special methods
# never calling them directly
# it only called when we initialize a new object

from typing import Self

class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        """Called every time we call len() function.
        You can implement any logic in this def"""
        return self.pages

    def __add__(self, other: Self) -> Self:
        combined_title: str = f"{self.title} & {other.title}"
        combined_pages: int = self.pages + other.pages

        return Book(combined_title, combined_pages)

def main() -> None:
    py_daily: Book = Book("PyDaily", 200)
    harry_potter: Book = Book("Harry Potter", 300)

    print(len(py_daily))
    print(len(harry_potter))

    # do not recommend this way
    # py_daily.__len__()

    # combined_books: Book = py_daily + harry_potter # Class Book does not define the dunder method, and so the + operator can not be used on its instances
    combined_books: Book = py_daily + harry_potter # Solution: define a dunder method (__add__) in class Book
    print(combined_books.title)
    print(combined_books.pages)
if __name__ == '__main__':
    main()