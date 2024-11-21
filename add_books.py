from Save_allBooks import Save_allBooks


def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn =int(input("Enter ISBN Number: "))
    year = int(input("Enter Publishing Year Number: "))
    price =float(input("Enter Book price: "))
    quantity=int(input("Enter Quantity Number: "))

    book={
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
       "quantity": quantity
    }

    all_books.append(book)
    Save_allBooks(all_books)
    print("Books Added Successfully")

    return all_books




