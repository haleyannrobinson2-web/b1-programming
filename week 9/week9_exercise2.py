# Library System with COmposition

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


# Library Class (Composition: contains Book objects)
class Library:
    def __init__(self):
        self.books = []  # list to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added successfully.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book "{title}" removed successfully.')
                return
        print(f'Book "{title}" not found.')

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(book.display_info())

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Book found:")
                print(book.display_info())
                return
        print(f'Book "{title}" not found.')


# -------------------------
# Testing the Library System
# -------------------------

# 1. Create library instance
library = Library()

# 2. Add at least 3 books
book1 = Book("1984", "George Orwell", "1111")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "2222")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "3333")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# 3. List all books
library.list_books()

# 4. Search for a specific book
library.search_book("1984")

# 5. Remove one book
library.remove_book("1984")

# Verify it's gone
library.list_books()