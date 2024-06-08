class Book:
    def __init__(self, title, author, ISBN, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = True

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__ISBN}, Genre: {self.__genre}, Published: {self.__publication_date}, Available: {'Yes' if self.__availability else 'No'}"

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        self.__availability = True

    
    def is_available(self):
        return self.__availability

    
    # Getters and Setters 
    def title(self):
        return self.__title

    def author(self):
        return self.__author

    def ISBN(self):
        return self.__ISBN

    def genre(self):
        return self.__genre

    def publication_date(self):
        return self.__publication_date

   
    def set_title(self, value):
        self.__title = value

    
    def set_author(self, value):
        self.__author = value

    
    def set_ISBN(self, value):
        self.__ISBN = value

   
    def set_genre(self, value):
        self.__genre = value

   
    def set_publication_date(self, value):
        self.__publication_date = value

    
