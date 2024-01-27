class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"\nBook: {self.title} \nAuthor: {self.author}\n"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book = Book("How to be a Lammer", "Lammer")
print(book)

book_2 = Book("How to be a real Hacker", "Hacker")
print(book_2)


print(f"The books are equal: {book == book_2}")
