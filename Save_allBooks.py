def Save_allBooks(all_books):
    with open("all_books.csv","w") as fp:
        for book in all_books:
            line = f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n"
            fp.write(line)