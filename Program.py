import datetime
import json


class Person:

    def __init__(self, name, lname, personal_id):
        self.name = name
        self.lname = lname
        self.personal_id = personal_id

    def __str__(self):
        return f"{self.name} {self.lname}"


class Book:

    def __init__(self, book_ID, title: str, author: str, publish_year: int, stock=1):
        self.Book_ID = book_ID
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.stock = stock

    def __str__(self):
        return f"{self.title} By {self.author}"


class LibraryManager:

    @staticmethod
    def add_book(book):
        if isinstance(book, Book):
            try:
                with open('Books.json', 'r') as file:
                    books = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                books = []

            new_book = {
                "ID": int(book.Book_ID),
                "Title": book.title.capitalize(),
                "Author": book.author.capitalize(),
                "Publish Year": int(book.publish_year),
                "Stock": int(book.stock)
            }
            books.append(new_book)
            with open('Books.json', 'w') as file:
                json.dump(books, file, indent=4)
            return "Book Added Successfully"
        else:
            return "This Isn't a Book Object"

    @staticmethod
    def display():
        with open('Books.json', 'r') as file:
            books = json.load(file)
            print("Available Books:\n")
            for each in books:
                print(f"{each['Title']} By {each['Author']} Published in {each['Publish Year']}")

    @staticmethod
    def search(title):
        with open('Books.json', 'r') as file:
            books = json.load(file)
            counter = 0
            while len(books) != counter:
                if books[counter]['Title'] == title:
                    if books[counter]['Stock'] == 0:
                        return f"This Book Is Out Of Stock"
                    book_id = books[counter]["ID"]
                    print(f"We Have This Book in Stock")
                    return [True, book_id]
                counter += 1
            else:
                return f"We Don't Have This Book"

    @staticmethod
    def book_return(identity: str):
        with open('Take_outs.json', 'r') as file:
            take_outs = json.load(file)
        for each in take_outs:
            if each['Customer_ID'] == identity:
                with open("Books.json", 'r') as file:
                    books = json.load(file)
                for book in books:
                    if book["ID"] == each["Book_ID"]:
                        book['Stock'] += 1
                        each["Status"] = "Returned"
                        break

                with open("Take_outs.json", 'w') as file:
                    json.dump(take_outs, file, indent=4)

                with open("Books.json", 'w') as file:
                    json.dump(books, file, indent=4)
                print(f"You Took {each['Title']} on {each["Taking Date"]}")

            else:
                return f"This Book Isn't From Our Library"

    @staticmethod
    def taking_book_out(personal_id: str, book_id: int):
        try:
            with open('costumer.json', 'r') as file:
                costumer = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            costumer = []  # validacia pirovnebis
        for each in costumer:
            if each['Personal_id'] == personal_id:
                with open('Books.json', 'r') as file:
                    books = json.load(file)
                for book in books:
                    if book["ID"] == book_id:
                        try:
                            with open('Take_outs.json', 'r') as file:
                                take_outs = json.load(file)
                            for take_out in take_outs:
                                if take_out["Customer_ID"] == personal_id and take_out["Status"] != "Returned":
                                    return "You Have To Return The Other Book First"
                        except (FileNotFoundError, json.decoder.JSONDecodeError):
                            take_outs = []

                        new_take_out = {
                            "Customer_ID": personal_id,
                            "Book_ID": book_id,
                            "Title": book["Title"],
                            "Taking Date": str(datetime.date.today()),
                            "Status": "Not Returned"
                        }

                        take_outs.append(new_take_out)

                        with open("Books.json", 'r') as file:
                            stock_update = json.load(file)
                        for stock in stock_update:
                            if stock["ID"] == book_id:
                                stock["Stock"] -= 1
                                break
                        with open("Books.json", 'w') as file:
                            json.dump(stock_update, file, indent=4)

                        with open('Take_outs.json', 'w') as file:
                            json.dump(take_outs, file, indent=4)
                            return "Order Complete"
            else:
                print("You Have To Register First")
                return False
