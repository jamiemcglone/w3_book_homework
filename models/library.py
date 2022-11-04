from models.book import Book

the_shining = Book("The Shining", "Stephen King", "Horror", False)
american_psycho = Book("American Psycho", "Bret Easton Ellis", "Dark Comedy", False)
the_sun_also_rises = Book("The Sun Also Rises", "Ernest Hemingway", "Fiction", False)
on_the_road = Book("On the Road", "Jack Kerouac", "Fiction", False)
the_big_sleep = Book("The Big Sleep", "Raymond Chandler", "Crime Fiction", True)
the_outsider = Book("The Outsider", "Albert Camus", "Fiction", True)

library_books = [the_shining, american_psycho, the_sun_also_rises, on_the_road, the_big_sleep, the_outsider]

def add_book_to_library(book_to_add):
    library_books.append(book_to_add)

def remove_book__from_library(book_to_remove_index):
    library_books.pop(book_to_remove_index)

def update_availability_status(book):
    book.checked_out = not book.checked_out
