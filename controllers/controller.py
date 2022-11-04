from flask import render_template, request, redirect
from app import app
from models.library import *
from models.book import Book


@app.route('/books')
def index():
    return render_template('index.html', title='Library', books=library_books)

@app.route('/books/<index>')
def individual_book(index):
    book_to_view = library_books[int(index) - 1]
    return render_template("book.html", title="View Book", book=book_to_view, books=library_books)

@app.route('/books', methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_book_to_library(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    remove_book__from_library(int(index) - 1)
    return redirect('/books')

@app.route('/books/<index>/status', methods=['POST'])
def update_status(index):
    book_to_update = library_books[(int(index) - 1)]
    update_availability_status(book_to_update)
    return redirect('/books')
