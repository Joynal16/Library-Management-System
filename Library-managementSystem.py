import add_books
import View_all_Books
from View_all_Books import View_all_books

all_books= []

while True:
    print("Welcome to library Management System")
    print("0.Exit")
    print("1. Add Books")
    print("2. View All Books")

    menu = input("Select any number: ")

    if menu=='0':
        print("Thanks for using Library Management System")
        break
    elif menu=='1':
      all_books= add_books.add_books(all_books)
    elif menu=='2':
       View_all_books(all_books)
    else:
        print("Choose a valid Number")
