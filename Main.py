from Books import Book
from Library import Library
from Movies import Movie
from Cd import Cd
import json
from appJar import gui

program_is_on = True
total_list = []
application_number = 0


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

while program_is_on == True:
    try:

        print(f"\n1. Add an object.  2. Show Library.  3. Show Library by media type.  4. Close Library\n")
        input_number = (input(f"Select an option: "))
        print("")

        if input_number == "1":
            media_type = input("What type of object do you want to register?(Book, movie or CD): ").lower()
            library_create_object = Library()
            library_create_object.create_object(media_type, total_list, dict_list)

        elif input_number == "2":
            print_library = Library()
            sorted_list = print_library.sorting_list(total_list)
            app = gui("Library", "400x200")
            app.startFrame(f"List{application_number}", row=5, column=0)
            app.addScrolledTextArea(f"Display{application_number}", text=None)
            app.addButton(f"Close{application_number}", app.stop, row=1, column=0)
            app.setTextArea(f"Display{application_number}", print_library.print_list(sorted_list), end= True, callFunction= True)
            app.go()
            application_number += 1

        elif input_number == "3":
            input_type = input("Enter type of media to be shown: ").lower()
            print_library_type = Library()
            sorted_list_type = print_library_type.sorting_list(total_list)
            print_library_type.print_list_by_type(input_type, sorted_list_type)

        elif input_number == "4":
            print("Library closed.")
            break
        else:
            raise ValueError(f"\n'{input_number}' is not an option")

    except ValueError as error:
        print(error)

with open("reg.json", "w") as close_file:
    json.dump(dict_list, close_file)
    close_file.close()




































