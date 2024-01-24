from modules.divider import divider


class Book:

    IVA = 0.21

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def bestseller(total_sales):
        return total_sales > 5000

    @classmethod
    def price_with_iva(cls, price):
        return price + (price * cls.IVA)


my_book = Book("Harry Potter", "J.K. Rowling", 29.99)
print(f"\n[+] The price with IVA is: {round(Book.price_with_iva(my_book.price), 2)}")


divider()


class DigitalBook(Book):

    IVA = 0.15

    def __init__(self, title, author, price, format_):
        super().__init__(title, author, price)
        self.format_ = format_


my_digital_book = DigitalBook("Harry Potter", "J.K. Rowling", 29.99, "PDF")
print(f"\n[+] The price with IVA is: {round(DigitalBook.price_with_iva(my_digital_book.price), 2)}")
