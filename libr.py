import json
import os
from termcolor import colored

# Sky blue theme setup
def sky_blue(text):
    return colored(text, 'cyan')

# Book class to hold book data
class Book:
    def __init__(self, title, author, year, genre, read):
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.year = year  # Year of publication
        self.genre = genre  # Genre of the book
        self.read = read  # Whether the book is read or not

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Read: {self.read}"

# Creating a book object with IT Course, year 2025
book = Book("IT Course", "Najma", 2025, "Education", True)

# Print the book details using the sky blue theme
print(sky_blue(str(book)))



def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'read': self.read
        }

# Library Manager
class LibraryManager:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = []
        self.load_library()

    def add_book(self, book):
        self.books.append(book)
        print(sky_blue("Book added successfully."))

    def remove_book(self, title):
        original_length = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        if len(self.books) < original_length:
            print(sky_blue("Book removed successfully."))
        else:
            print(sky_blue("Book not found."))

    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        for book in results:
            self.display_book(book)
        if not results:
            print(sky_blue("No books found matching your query."))

    def display_book(self, book):
        read_status = 'Read' if book.read else 'Unread'
        print(sky_blue(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Status: {read_status}"))

    def show_statistics(self):
        total = len(self.books)
        read_books = len([book for book in self.books if book.read])
        unread_books = total - read_books
        print(sky_blue(f"Total Books: {total}"))
        print(sky_blue(f"Read Books: {read_books}"))
        print(sky_blue(f"Unread Books: {unread_books}"))

    def save_library(self):
        with open(self.filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f)
        print(sky_blue("Library saved successfully."))

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
                print(sky_blue("Library loaded successfully."))
        else:
            self.books = []

# Main menu

def main():
    manager = LibraryManager()

    while True:
        print(sky_blue("\n--- Personal Library Manager ---"))
        print(sky_blue("1. Add Book"))
        print(sky_blue("2. Remove Book"))
        print(sky_blue("3. Search Books"))
        print(sky_blue("4. Show Statistics"))
        print(sky_blue("5. Save Library"))
        print(sky_blue("6. Exit"))

        choice = input(sky_blue("Enter your choice: "))

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Publication Year: "))
            genre = input("Genre: ")
            read_input = input("Have you read it? (yes/no): ").strip().lower()
            read = True if read_input == 'yes' else False
            book = Book(title, author, year, genre, read)
            manager.add_book(book)

        elif choice == '2':
            title = input("Enter title to remove: ")
            manager.remove_book(title)

        elif choice == '3':
            query = input("Enter title or author to search: ")
            manager.search_books(query)

        elif choice == '4':
            manager.show_statistics()

        elif choice == '5':
            manager.save_library()

        elif choice == '6':
            manager.save_library()
            print(sky_blue("Exiting program. Goodbye!"))
            break

        else:
            print(sky_blue("Invalid choice. Please try again."))

if __name__ == '__main__':
    main()


