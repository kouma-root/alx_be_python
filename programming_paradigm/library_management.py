class Book:
    def __init__(self, title, author):
        
        self.title = title
        self.author = author
        self.__is_checked_out = 0
        


class Library:
    def __init__(self):
        self.__book = []
        self.__checked_out_books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.__book.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library.")
    def list_available_books(self):
        available_books = [book for book in self.__book if book._Book__is_checked_out == 0]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
    def check_out_book(self, title):
        for book in self.__book:
            if book.title == title and book._Book__is_checked_out == 0:
                book._Book__is_checked_out = 1
                self.__checked_out_books.append(book)
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available for checkout.")
    def return_book(self, title):
        for book in self.__checked_out_books:
            if book.title == title:
                book._Book__is_checked_out = 0
                self.__checked_out_books.remove(book)
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out from this library.")
    def is_checked_out(self):
        return any(book._Book__is_checked_out == 1 for book in self.__book)
    def get_checked_out_books(self):
        return [book for book in self.__checked_out_books if book._Book__is_checked_out == 1]
        # Initialize the book as not checked out
        self.__is_checked_out = 0       