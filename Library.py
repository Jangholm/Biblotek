from Books import Book
from Movies import Movie
from Cd import Cd

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
                print(f"Add book \n")
                default_object.create_book(default_object)
                if not default_object.Title or not default_object.Author:
                    raise ValueError("\nInvalid title or author! Object not added to the library.")
                default_object.check_object_year()
                default_object.object_dict(dict_list)
                default_object.dict_price()
                lista.append(default_object)
                print(f"Object added succesfully in '{type}'")
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
                print(f"Object added succesfully in '{type}'")
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
                print(f"Object added succesfully in '{type}'")
                return default_object
            else:
                print(f"\nThe media type '{type}' doesn't exist in the library")

        except ValueError as error:
            print(error)


