# Single Responsibility Principle



# bad
class Book:
    inventory = []
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.add_to_inventory()
        
    def add_to_inventory(self):
        self.inventory.append(self)
        
    def remove_from_inventory(self):
        self.inventory.remove(self)

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")


# ------------------------------------------------------------


# good
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)