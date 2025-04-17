

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: "Book") ->str:
        self.books.append(book)
        return f"The book name is {book.book_name}, authored by {book.author} with ibn code {book.ibn_code},  added to library."


    def list_books(self) ->str:
        if not self.books:
            return f"No books in {Library}"
        return "\n".join([book.book_return() for book in self.books])

    def search_books(self, query: str) -> str:
        results = [
            book.book_return()
            for book in self.books
            if query.lower() in book.book_name.lower()
               or query.lower() in book.author.lower()
               or query in str(book.ibn_code)
        ]

        if results:
            return f"The query '{query}' returned the following books:\n" + "\n".join(results)
        else:
            return  f"No books found for the query '{query}'."

class Book:
    total_books = 0
    publisher = "abc productions"

    def __init__(self, book_name: str, author: str, ibn_code: int) -> None:
        self.book_name = book_name
        self.author = author
        self.ibn_code = ibn_code
        Book.total_books += 1

    def book_return(self) -> str:
        return f"The book name is {self.book_name}, authored by {self.author} with ibn code {self.ibn_code}"

book1 = Book("the book of fola", "fola ogundero", 26786876786)
book2 = Book("Atomic Habbits", "John Smith", 12378912937218)

TheWorldLibrary = Library()

print(TheWorldLibrary.add_book(book1))
print(TheWorldLibrary.add_book(book2))
print(TheWorldLibrary.search_books("Fola"))
print(TheWorldLibrary.search_books("123789"))  # partial ibn_code
print("Done")
print(TheWorldLibrary.list_books())


