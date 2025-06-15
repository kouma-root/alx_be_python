class Book:
    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self.__is_checked_out = 0
    def return_book(self):
        if self.__is_checked_out == True:
            self.__is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")
        


class Library:
    def __init__(self):
        self._books = []
        self._checked_out_books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library.")
    def list_available_books(self):
        available_books = [book for book in self._books if book._Book__is_checked_out == 0]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._Book__is_checked_out == 0:
                book._Book__is_checked_out = 1
                self._checked_out_books.append(book)
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available for checkout.")
    def return_book(self, title):
        for book in self.__checked_out_books:
            if book.title == title:
                book.return_book()
                self._checked_out_books.remove(book)
                return
        print(f"Book '{title}' was not checked out from this library.") 