"""
Program to understand class
"""


# Initialization

class Book:  # Initialization of class
    def __init__(self, title, author):  # Constructor
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"


my_book1 = Book("The secret", "Rhonda Bryne")  # Object or instance of a class
my_book2 = Book("Hold my Hand", "Durjoy Dutta")  # Object or instance of a class

print(my_book1.display_info(),"\n",my_book2.display_info())
