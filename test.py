import unittest
import server

class Test_Server(unittest.TestCase):

    def test_book(self):
        self.book = server.Book("Harry Potter", "Rowling", 400, 100, 2000)

        self.assertEqual(self.book.Title, "Harry Potter")

        self.book.Title = "James Bond"

        self.assertEqual(self.book.Title, "James Bond")

if __name__ == "__main__":
    unittest.main()

