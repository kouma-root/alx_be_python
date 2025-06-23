class Book:
    def __init__(self,title,author) -> None:
        self.title = title
        self.author = author
        
    
class EBook(Book):
    def __init__(self, title, author,file_size) -> None:
        super().__init__(title, author)
        self.file_size = file_size
        

class PrintBook(Book):
    def __init__(self, title, author,page_count) -> None:
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self, books=None) -> None:
        if books is None:
            books = []
        self.books = books
        
    def add_book(self, book):
        self.books.append(book)
        
    def __str__(self) -> str:
        return f"Library with {len(self.books)} books."
    
    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")