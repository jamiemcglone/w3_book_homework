from models.book import Book
from models.library import *
import unittest

class TestBook(unittest.TestCase):

    def test_book_has_title(self):
        self.assertEqual("The Shining", library_books[0].title)

    
    def test_book_has_author(self):
        self.assertEqual("Stephen King", library_books[0].author)

    
    def test_book_has_genre(self):
        self.assertEqual("Horror", library_books[0].genre)


    def test_can_add_book(self):
        into_the_wild = Book("Into the Wild", "Jon Karkauer", "Non-fiction")
        add_book_to_library(into_the_wild)
        self.assertEqual(7, len(library_books))

    def test_can_remove_book(self):
        remove_book__from_library(3)
        self.assertEqual(6, len(library_books))

