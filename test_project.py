# test_project.py

import pytest
from project import add_book, search_books_by_title, search_books_by_author, list_books, Book

def test_add_book():
    collection = []
    add_book(collection, "Book Title", "Book Author")
    assert len(collection) == 1
    assert collection[0] == Book("Book Title", "Book Author")

def test_search_books_by_title():
    collection = [
        Book("Title One", "Author One"),
        Book("Title Two", "Author Two")
    ]
    result = search_books_by_title(collection, "Title One")
    assert len(result) == 1
    assert result[0].title == "Title One"

def test_search_books_by_author():
    collection = [
        Book("Title One", "Author One"),
        Book("Title Two", "Author One")
    ]
    result = search_books_by_author(collection, "Author One")
    assert len(result) == 2
    assert all(book.author == "Author One" for book in result)

def test_list_books():
    collection = [
        Book("Title One", "Author One"),
        Book("Title Two", "Author Two")
    ]
    result = list_books(collection)
    assert len(result) == 2
    assert result == ["'Title One' by Author One", "'Title Two' by Author Two"]
