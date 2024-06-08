class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def view_details(self):
        return f"Genre Details:\nName: {self.name}, Description: {self.description}, Category: {self.category}"
    
    def __str__(self):
        return f"Genre: {self.name}, Description: {self.description}, Category: {self.category}"

    
    # getters
    def name(self):
        return self.name
    
    def description(self):
        return self.description
    
    def category(self):
        return self.category
    
    # setters
    def set_name(self, value):
        self.name = value

    def set_description(self, value):
        self.description = value

    def set_biography(self, value):
        self.biography = value