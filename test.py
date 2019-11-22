import unittest
import server

class Test_Server(unittest.TestCase):

    def setUp(self):
        print("SetUp")

    def tearDown(self):
        print("TearDown")

    def test_book(self):
        print("test_book")
        book = server.Book("Harry Potter", "Rowling", 400, 100, 1998)
        self.assertEqual(book.Title, "Harry Potter")
        book.Title = "James Bond"
        self.assertEqual(book.Title, "James Bond")
    def test_movie(self):
        print("test_movie")
        movie = server.Movie("Lord of the Rings", "Tolkein", 120, 50, 2000)
        self.assertEqual(movie.Title, "Lord of the Rings")
        movie.Title = "hah"
        self.assertEqual(movie.Title, "hah")
    def test_cd(self):
        print("test_cd")
        cd = server.Cd("Detroit", "Kiss", 10, 60, 100)
        self.assertEqual(cd.Title, "Detroit")
        cd.Title = "blah"
        self.assertEqual(cd.Title, "blah")
    def test_library_list(self):
        print("test_library_list")
        book = server.Book("Harry Potter", "Rowling", 400, 100, 1998)
        movie = server.Movie("Lord of the Rings", "Tolkein", 120, 50, 2000)
        cd = server.Cd("Detroit", "Kiss", 10, 60, 100)
        test_list = [book, movie, cd]
        library = server.Library()
        sorted_list = library.sorting_list(test_list)
        self.assertEqual(sorted_list, [cd, book, movie])

if __name__ == "__main__":
    unittest.main()

