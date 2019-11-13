class Cd():
    """Default värderna för ett cd objekt"""
    def __init__(self, title = "", artist = "", songs = 0, length = 0, purchase_price = 0):
        self.Title = title
        self.Artist = artist
        self.Songs = songs
        self.Length = length
        self.Purchase_price = purchase_price
        self.type = "cd"


    def __str__(self):
        return "Title: {}\nArtist: {}\nSongs: {}\nLength: {}\nPurchase price: {}\nType: {}\n".format(self.Title, self.Artist, self.Songs, self.Length, self.Purchase_price, self.type)

    def create_cd(self, cd):
        """Skapar cd objekt"""

        print(f"Add cd \n")
        input_title = input("Enter the name of the cd: ")
        input_artist = input("Enter the artist: ")
        input_songs = int(input("Enter the amount of songs: "))
        input_length = input("Enter the duration (min): ")
        input_purchase_price = int(input("Enter purchase price: "))

        self.Title = input_title
        self.Artist = input_artist
        self.Length = input_length
        self.Songs = input_songs
        self.Purchase_price = input_purchase_price
        self.type = "cd"
        self.dict = {"Title": input_title, "Artist": input_artist, "Length": input_length,
                     "Purchase price": input_purchase_price, "Songs": input_songs,
                     "Type": "cd"}

    def object_dict(self, list):
        """Lägger till objektets dikt i dict_list"""
        list.append(self.dict)

    def check_object_value(self, list):
        """Priset som användaren skrev in ska delas på antalet 'cd' objekt som har samma
            värden i 'Title' och 'Artist' och det objekt användaren har skapat."""
        amount = 0
        for cd in list:
            if cd["Type"] == "cd" and self.dict["Title"] in cd["Title"] and self.dict["Artist"] in cd["Artist"]:
                amount +=1

        self.Purchase_price = self.Purchase_price // amount
        return self.Purchase_price

    def dict_price(self):
        """Lägger till det nya korrigerade priset i objektets dikt värde 'Purchase Price'."""
        self.dict["Purchase price"] = self.Purchase_price


