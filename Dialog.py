import json

from Program import LibraryManager, Person


print("Welcome To Our Library \nHow Can I Help You ? ")

while True:
    try:
        choice = int(input("""
1) Looking For a Book
2) Returning a Book
3) Want To See All The Books
4) Register
"""))
        if 1 <= choice <= 4:
            break
        else:
            print("Please Enter Number Again")
    except ValueError as v:
        print("Please Enter Valid Number")


if choice == 1:
    book = input("Which Book Are You Looking For Exactly: ").capitalize()
    ans = LibraryManager.search(title=book)
    if ans[0] is True:
        answer = input("Do You Want To Take Out This Book ? [YES/NO]\n")
        if answer.lower().strip() == "yes":
            true = True
            while true is True:
                identity = input("Your Personal ID number: ")
                if len(identity) == 11 and identity.isdigit() is True:
                    try:
                        with open('costumer.json', 'r') as file:
                            costumers = json.load(file)
                        for each in costumers:
                            if each["Personal_id"] != identity:
                                print("""You Are Not Registered !
Please Register First""")
                                true = False
                                break
                            else:
                                print(LibraryManager.taking_book_out(identity, ans[1]))
                                true = False
                    except (FileNotFoundError, json.decoder.JSONDecodeError):
                        print("""You Are Not Registered !
                        Please Register First""")
                        true = False
                else:
                    print("Provide Your ID Correctly: ")
    else:
        print("Book Is Out Of Stock")


elif choice == 2:
    while True:
        personal_id = input("Your ID Number Please: ")
        if len(personal_id) == 11 and personal_id.isdigit() is True:
            break
        else:
            print("Please Provide Your ID Correctly")
    LibraryManager.book_return(personal_id)


elif choice == 3:
    print("Let's Find One For You: ")
    LibraryManager.display()

elif choice == 4:
    name = input("Enter Your Name: ")
    lname = input("Enter Your LastName: ")
    true = True
    while true is True:
        personal_id = input("Enter Your Personal ID Number: ")
        if len(personal_id) == 11 and personal_id.isdigit() is True:
            try:
                with open('costumer.json', 'r') as file:
                    costumers = json.load(file)
                for each in costumers:
                    if each["Personal_id"] == personal_id:
                        print("You Are Registered !")
                        true = False
                        break
                    else:
                        print("This ID Is Already Registered")
                        true = False
                        break
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                costumer = []
                Person(name, lname, personal_id)
                new_costumer = {
                    "Name": name,
                    "Lname": lname,
                    "Personal_id": personal_id
                }
                costumer.append(new_costumer)
                with open('costumer.json', 'w') as file:
                    json.dump(costumer, file, indent=4)
                break
        else:
            print("Provide Your ID Number Correctly")
