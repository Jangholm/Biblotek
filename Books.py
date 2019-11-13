import datetime

class Book():
    """Default värderna för ett book objekt"""
    def __init__(self, Title = "none", Author = "none", Pages = 0 , Purchase_price = 0, Purchase_year = 0):
        self.Title = Title
        self.Author = Author
        self.Pages = Pages
        self.Purchase_price = Purchase_price
        self.Purchase_year = Purchase_year
        self.type = "book"

    def __str__(self):
        return "Title: {}\nAuthor: {}\nPages: {}\nPurchase Price: {}\nPurchase Year: {}\nType: {}\n".format(self.Title, self.Author, self.Pages, self.Purchase_price, self.Purchase_year, self.type)

    def create_book(self, book):
        """Skapar bok objekt"""

        input_title = input("Enter the name of the book: ")
        input_author = input("Enter the author:")
        input_pages = int(input("Enter amount of pages:"))
        input_purchase_price = int(input("Enter purchase price:"))
        input_purchase_year = int(input("Enter purchase year: "))

        self.Title = input_title
        self.Author = input_author
        self.Pages = input_pages
        self.Purchase_price = input_purchase_price
        self.Purchase_year = input_purchase_year
        self.type = "book"
        self.dict = {"Title": input_title, "Author": input_author, "Pages": input_pages, "Purchase price": input_purchase_price,
                     "Purchase year": input_purchase_year, "Type": "book"}

    def object_dict(self, list):
        """Lägger till objektets dikt i dict_list"""
        list.append(self.dict)

    def check_object_year(self):
        """Kollar årsskillnaden och räknar ut priset beroende på om  årsskillnaden är under 50 eller över 50.
           Tog hjälp av klasskamrater för att lösa uträkningarna."""
        book_year = self.Purchase_year
        current_year = datetime.date.today()
        year_difference = current_year.year - book_year

        if year_difference <= 50:
            self.Purchase_price = self.Purchase_price * 0.9 **year_difference
            return self.Purchase_price
        elif year_difference > 50:
            for _ in range(50):
                minus = self.Purchase_price * 10/100
                self.Purchase_price = self.Purchase_price - minus
            new_year_difference = year_difference - 50
            for _ in range(new_year_difference):
                plus = self.Purchase_price * 8/100
                self.Purchase_price = self.Purchase_price + plus

            return self.Purchase_price

    def dict_price(self):
        """Lägger till det nya korrigerade priset i objektets dikt värde 'Purchase Price'."""
        self.dict["Purchase price"] = self.Purchase_price
























