class Book:

    IVA = 0.21

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def bestseller(total_sales):
        return total_sales > 5000

    @staticmethod
    def price_with_iva(price):
        return price + (price * Book.IVA)


my_book = Book("Harry Potter", "J.K. Rowling", 29.99)
print(
    f"\n[+] The price with IVA is: {round(Book.price_with_iva(my_book.price), 2)}")
