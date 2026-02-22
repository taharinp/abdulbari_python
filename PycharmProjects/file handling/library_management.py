import os

FILENAME = "library.dat"
RECORD_SIZE = 50   # Fixed size record


# Add Book
def add_book():

    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")

    record = book_id + "," + book_name

    record = record.ljust(RECORD_SIZE)

    file = open(FILENAME, "ab")
    file.write(record.encode())
    file.close()

    print("Book Added Successfully")


# View Books
def view_books():

    try:
        file = open(FILENAME, "rb")

        while True:

            data = file.read(RECORD_SIZE)

            if not data:
                break

            record = data.decode().strip()

            print(record)

        file.close()

    except:
        print("No Records Found")


# Search Book using Random Access
def search_book():

    position = int(input("Enter Record Number: "))

    try:

        file = open(FILENAME, "rb")

        file.seek(position * RECORD_SIZE)

        data = file.read(RECORD_SIZE)

        record = data.decode().strip()

        print("Record Found:", record)

        file.close()

    except:

        print("Error")


# Menu
while True:

    print("\n1 Add Book")
    print("2 View Books")
    print("3 Search Record")
    print("4 Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        add_book()

    elif ch == "2":
        view_books()

    elif ch == "3":
        search_book()

    elif ch == "4":
        break

    else:
        print("Invalid Choice")