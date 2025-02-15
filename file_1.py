def book_dictionary():
    books = []
    for i in range(5):
        author = input(f"Книга({i+1}) Введите автора: ")
        title = input(f"Книга({i+1}) Введите заголовок: ")
        book = { "Автор": author, "Заголовок": title }
        books.append(book)
    print(books)

book_dictionary()
