class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # def __del__(self):
    #     print(f"Deleting {self.title}")

    # def __str__(self):
    #     return f"{self.title} by {self.author}, published in {self.year}"

    # def __repr__(self):
    #     return f"Book('{self.title}', '{self.author}', {self.year})"
    
class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
    
class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count
        
class Library(Book):
    def __init__(self, books):
        self.books = {}
        
    def add_book(self, book):
        Book.title = "nbb"
        Book.author = "popo"