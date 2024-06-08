class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def __str__(self) -> str:
        return f"Author: {self.name}, Biography: {self.biography}"
    
    def view_details(self):
        return f"User Details:\nName: {self.name}, Biography: {self.biography}"
    
    # Getters and Setters for encapsulation
    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

    @name.setter
    def name(self, value):
        self.__name = value

    @biography.setter
    def biography(self, value):
        self.__biography = value