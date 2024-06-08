from book import Book


books = []

def book_operations():
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_new_book()
            elif choice == '2':
                borrow_book()
            elif choice == '3':
                return_book()
            elif choice == '4':
                search_book()
            elif choice == '5':
                display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

def add_new_book():
    title = input("Enter a title: ")
    author = input("Enter an author: ")
    ISBN = input("Enter ISBN #: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    new_book = Book(title, author, ISBN, genre, publication_date)
    books.append(new_book)
    print(f"Book '{title}' added successfully!")

def borrow_book():
    book_title = input("Enter the name of the book you want to borrow: ")
    for book in books:
        if book.title().lower() == book_title.lower():
            if book.borrow():
                print(f"You have borrowed '{book_title}'.")
            else:
                print(f"'{book_title}' is currently not available.")
            return
    print(f"Book '{book_title}' not found.")

def return_book():
    book_title = input("Enter the name of the book you want to return: ")
    for book in books:
        if book.title().lower() == book_title.lower():
            book.return_book()
            print(f"You have returned '{book_title}'.")
            return
    print(f"Book '{book_title}' not found.")

def search_book():
    search_term = input("Enter the title or ISBN of the book to search: ")
    for book in books:
        if book.title().lower() == search_term.lower() or book.ISBN() == search_term:
            print(book)
            return
    print(f"Book '{search_term}' not found.")

def display_all_books():
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(book)