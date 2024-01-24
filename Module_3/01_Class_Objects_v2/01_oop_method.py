class Book:

    def __init__(self, title, author, price, bestseller_value=5000):
        self.title = title
        self.author = author
        self.price = price
        self.bestseller_value = bestseller_value

    @staticmethod
    def bestseller(instance, sales):
        return sales > instance.bestseller_value


my_book = Book("Harry Potter", "J.K. Rowling", 29.99)
print(my_book.bestseller(my_book, 10000))  # True
print(my_book.bestseller(my_book, 1000))  # False
