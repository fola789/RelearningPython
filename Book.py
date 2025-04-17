class Book:
    total_books = 0
    publisher = "abc productions"
    def __init__(self, book_name: str, author: str, ibn_code: int) ->None:
        self.book_name = book_name
        self.author = author
        self.ibn_code  = ibn_code
        Book.total_books +=1

    def book_return(self) ->str:
        return f"The book name is {self.book_name}, authored by {self.author} with ibn code {self.ibn_code}"

book1 = Book("the book of fola","fola ogundero" ,26786876786)
book2 = Book("Atomic Habbits","John Smith" ,12378912937218)

print(book1.book_return())
print(book1.publisher)
print(book2.book_return())
print(book2.publisher)