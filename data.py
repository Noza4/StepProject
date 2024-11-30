import json

from Program import Book, LibraryManager

try:
    with open("Books.json", 'r') as file:
        books = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    books = []


book1 = Book(1, 'Test1', "Test_Author1", 2024, 10)
book2 = Book(2, 'Test2', "Test_Author2", 2023, 5)
book3 = Book(3, 'Test3', "Test_Author3", 2022, 0)
book4 = Book(4, 'Test4', "Test_Author4", 2021)
book5 = Book(5, 'Test5', "Test_Author5", 2020)

LibraryManager.add_book(book1)
LibraryManager.add_book(book2)
LibraryManager.add_book(book3)
LibraryManager.add_book(book4)
LibraryManager.add_book(book5)
