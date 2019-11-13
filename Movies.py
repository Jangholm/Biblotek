import datetime

class Movie():
    """Default värderna för ett film objekt"""
    def __init__(self, Title = "None", Director = "None", Length = 0, Purchase_price = 0, Purchase_year = 0):
        self.Title = Title
        self.Director = Director
        self.Length = Length
        self.Purchase_price = Purchase_price
        self.Purchase_year = Purchase_year
        self.type = "movie"

    def __str__(self):
        return "Title: {}\nDirector: {}\nLength: {}\nPurchase Price: {}\nPurchase Year: {}\nType: {}\n".format(self.Title, self.Director,
                                                                                                self.Length,
                                                                                                self.Purchase_price,
                                                                                                self.Purchase_year,self.type)

    def create_movie(self, movie):
        """Skapar film objekt"""

        print(f"Add movie \n")
        input_title = input("Enter the name of the movie: ")
        input_director = input("Enter the director: ")
        input_length = int(input("Enter the duration (min): "))
        input_purchase_price = int(input("Enter purchase price: "))
        input_purchase_year = int(input("Enter purchase year: "))

        self.Title = input_title
        self.Director = input_director
        self.Length = input_length
        self.Purchase_price = input_purchase_price
        self.Purchase_year = input_purchase_year
        self.type = "movie"
        self.dict = {"Title": input_title, "Director": input_director, "Length": input_length,
                     "Purchase price": input_purchase_price,
                     "Purchase year": input_purchase_year, "Type": "movie"}
    def check_object_year(self):
        """Kollar årsskillnaden och beräknar priset på filmen utifrån det skick på filmen
           som användaren matar in och årsskillnaden.
           Tog hjälp av klasskamrater för att lösa uträkningarna."""
        movie_year = self.Purchase_year
        current_year = datetime.date.today()
        year_difference = current_year.year - movie_year
        value = 0
        while value == 0 or value > 10:
            value = int(input("Enter the value of the movie '1 to 10' (1= very bad, 10= very good): "))
        reduction = value * 0.1
        self.Purchase_price = self.Purchase_price * (0.9**year_difference) * reduction
        return self.Purchase_price

    def object_dict(self, list):
        """Lägger till objektets dikt i 'dict_list'."""
        list.append(self.dict)

    def dict_price(self):
        """Lägger till det nya korrigerade priset i objektets dikt värde 'Purchase Price'."""
        self.dict["Purchase price"] = self.Purchase_price

