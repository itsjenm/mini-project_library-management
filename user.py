from book import Book

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
    
    def __str__(self):
        return f"User: {self.__name}, Library ID: {self.__library_id}, Borrowed books: {self.__borrowed_books}"
    
    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)
            return True 
        return False

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        return False

    def view_details(self):
        return f"User Details:\nName: {self.__name}\nLibrary ID: {self.__library_id}\nBorrowed Books: {', '.join(self.__borrowed_books) if self.__borrowed_books else 'None'}"
    

    # Getters and setter for encapsulation
    def name(self):
        return self.__name
    
    def library_id(self):
        return self.__library_id
    
    def borrowed_books(self):
        return self.__borrowed_books
    
    def set_name(self, value):
        self.__name = value

    def set_library_id(self, value):
        self.__library_id = value

    