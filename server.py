from Books import Book
from Library import Library
from Movies import Movie
from Cd import Cd
import json
from appJar import gui
import socket
from threading import Thread
import datetime


total_list = []


""" Öppnar json filen där objekten från förra programkörningen finns lagrade som dikter,
    och för över de till listan 'dict_list'. För att sedan lägga till de i listan 'total_list'
    som är listan som senare kommer att sorteras in i en variabel och printas när användaren 
    vill öppna bibloteket, så skapas nya objekt av de dikter som finns i 'dict_list'. 
    Dessa objekt läggs sedan till i 'total_list'."""
with open("reg.json", "r") as open_file:
    dict_list = json.load(open_file)
    for item in dict_list:
        if item["Type"] == "book":
            default_book = Book()
            default_book.Title = item["Title"]
            default_book.Author = item["Author"]
            default_book.Pages = item["Pages"]
            default_book.Purchase_price = item["Purchase price"]
            default_book.Purchase_year = item["Purchase year"]
            default_book.type = "book"
            total_list.append(default_book)
        elif item["Type"] == "movie":
            default_movie = Movie()
            default_movie.Title = item["Title"]
            default_movie.Director = item["Director"]
            default_movie.Length = item["Length"]
            default_movie.Purchase_price = item["Purchase price"]
            default_movie.Purchase_year = item["Purchase year"]
            default_movie.Type = "movie"
            total_list.append(default_movie)
        elif item["Type"] == "cd":
            default_cd = Cd()
            default_cd.Title = item["Title"]
            default_cd.Artist = item["Artist"]
            default_cd.Length = item["Length"]
            default_cd.Purchase_price = item["Purchase price"]
            default_cd.Songs = item["Songs"]
            default_cd.Type = "cd"
            total_list.append(default_cd)

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

        conn.sendall(f"Add cd \n".encode())
        conn.sendall("Enter the name of the cd: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_title = data
        conn.sendall("Enter the artist: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_artist = data
        conn.sendall("Enter the amount of songs: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_songs = int(data)
        conn.sendall("Enter the duration (min): ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_length = data
        conn.sendall("Enter purchase price: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_purchase_price = int(data)

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

        conn.sendall(f"Add movie \n".encode())
        conn.sendall("Enter the name of the movie: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_title = data
        conn.sendall("Enter the director: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_director = data
        conn.sendall("Enter the duration (min): ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_length = int(data)
        conn.sendall("Enter purchase price: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_purchase_price = int(data)
        conn.sendall("Enter purchase year: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_purchase_year = int(data)

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
            conn.sendall("Enter the value of the movie '1 to 10' (1= very bad, 10= very good): ".encode())
            data = conn.recv(1024)
            value = int(data)
        reduction = value * 0.1
        self.Purchase_price = self.Purchase_price * (0.9**year_difference) * reduction
        return self.Purchase_price

    def object_dict(self, list):
        """Lägger till objektets dikt i 'dict_list'."""
        list.append(self.dict)

    def dict_price(self):
        """Lägger till det nya korrigerade priset i objektets dikt värde 'Purchase Price'."""
        self.dict["Purchase price"] = self.Purchase_price

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

        conn.sendall("Enter the name of the book: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_title = data
        conn.sendall("Enter the author: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_author = data
        conn.sendall("Enter amount of pages:".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_pages = int(data)
        conn.sendall("Enter purchase price:".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_purchase_price = int(data)
        conn.sendall("Enter purchase year: ".encode())
        data = conn.recv(1024)
        data = data.decode()
        input_purchase_year = int(data)

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

class Library():
    def print_list_by_type(self, type, lista):
        for item in lista:
            if item.type == type:
                print(item)

    def sorting_list(self, list):
            sort_list = sorted(list, key=lambda x: x.Title, reverse=False)
            return sort_list

    def print_list(self, list):
        return "\n".join([str(obj) for obj in list])

    def create_object(self, type, lista, dict_list):
        """Skapar ett default objekt som sedan skickas in i funktioner som gör att:
            användaren kan skriva över dess attributer via input, korrigerar priset,
            lägger till objektets dikt i 'dict_list', och lägger till objektet i total_list."""
        try:
            if type == "book":
                default_object = Book()
                conn.sendall(f"Add book: ".encode())
                default_object.create_book(default_object)
                if not default_object.Title or not default_object.Author:
                    raise ValueError("\nInvalid title or author! Object not added to the library.")
                default_object.check_object_year()
                default_object.object_dict(dict_list)
                default_object.dict_price()
                lista.append(default_object)
                conn.sendall(f"Object added succesfully in '{type}'".encode())
                return default_object
            elif type == "movie":
                default_object = Movie()
                default_object.create_movie(default_object)
                if not default_object.Title or not default_object.Director:
                    raise ValueError("\nInvalid title or author! Object not added to the library.")
                default_object.check_object_year()
                default_object.object_dict(dict_list)
                default_object.dict_price()
                lista.append(default_object)
                conn.sendall(f"Object added succesfully in '{type}'".encode())
                return default_object
            elif type == "cd":
                default_object = Cd()
                default_object.create_cd(default_object)
                if not default_object.Title or not default_object.Artist:
                    raise ValueError("\nInvalid title or artist! Object not added to the library.")
                default_object.object_dict(dict_list)
                default_object.check_object_value(dict_list)
                default_object.dict_price()
                lista.append(default_object)
                conn.sendall(f"Object added succesfully in '{type}'".encode())
                return default_object
            else:
                print(f"\nThe media type '{type}' doesn't exist in the library")
        except ValueError as error:
            print(error)

def broadcast(data):
    data = data.lower()
    if data == "1":
        text = "What type of object do you want to register?(Book, movie or CD): "
        conn.sendall(text.encode())
        data = conn.recv(1024)
        data = data.decode()
        library_create_object = Library()
        library_create_object.create_object(data, total_list, dict_list)
        print(f"A {data} was added in the Library by {adress}")
    elif data == "2":
        print_library = Library()
        sorted_list = print_library.sorting_list(total_list)
        print(sorted_list)
        new = print_library.print_list(sorted_list)
        for book in new:
            conn.sendall(book.encode())

def recive(conn):
    while True:
        try:
            conn.sendall(f"\n1. Add an object.  2. Show Library.  \n Select an option: ".encode())
            data = conn.recv(1024)
            data = data.decode()
            if not data:
                break
            elif data == "quit":
                conn.sendall(data.encode())
                break
            broadcast(data)
        except Exception:
            break
    conn.close()
    with open("reg.json", "w") as close_file:
        json.dump(dict_list, close_file)
        close_file.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.20.201.140", 65432))
server.listen()

while True:
    conn, adress = server.accept()
    myThread = Thread(target=recive, args=(conn,), daemon=True)
    myThread.start()







































