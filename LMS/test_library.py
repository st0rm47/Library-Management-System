import pytest
from library import Library
from library import Book
from library import Member

#Testing to add a book
def test_add_book1():
    lib = Library()
    book1 = Book("DSA", "Sukraj Neyong", "123456789", True)
    lib.add_book(book1)
    assert lib.books == [book1]

def test_add_book2():
    lib = Library()
    book2 = Book("CA", "Kiran Bagale", "987654321" , True)
    lib.add_book(book2)
    assert lib.books == [book2]
    
#Testing to remove a book
def test_remove_book():
    lib = Library()
    lib.remove_book("123456789")
    assert lib.books == []

#Testing to add a member
def test_add_member1():
    lib = Library()
    member1 = Member("Subodh", "1", "9860443449")
    lib.add_member(member1)
    assert lib.members == [member1]

#Testing to add a member
def test_add_member2():
    lib = Library()
    member2 = Member("Firoj", "2", "9860443448")
    lib.add_member(member2)
    assert lib.members == [member2]
    
#Testing to remove a member
def test_remove_member():
    lib = Library()
    lib.remove_member("2")
    assert lib.members == []
    
#Testing to borrow a book
def test_borrow_book():
    lib = Library()
    book = Book("NM", "Mohit Guragain", "789456123", True)
    lib.add_book(book)
    member = Member("Famous", "3", "9876543210")
    lib.add_member(member)
    lib.borrow_book("3", "789456123")
    assert book.availability == False

#Testing to return a book   
def test_return_book():
    lib = Library()
    book = Book("NM", "Mohit Guragain", "789456123", False)
    lib.add_book(book)
    member = Member("Famous", "3", "9876543210")
    lib.add_member(member)
    lib.borrow_book("3", "789456123")
    lib.return_book("3", "789456123")
    assert book.availability == True

#Testing to display a book   
def test_display_book():
    lib = Library()
    book = Book("NM", "Mohit Guragain", "789456123", True)
    lib.add_book(book)
    result = lib.display_book()
    assert result == "Title: NM, Author: Mohit Guragain, ISBN: 789456123, Availability: Available\n"

#Testing to display a member
def test_display_member():
    lib = Library()
    member = Member("Famous", "3", "9876543210")
    lib.add_member(member)
    result = lib.display_member()
    assert result == "Name: Famous, Member ID: 3, Phone Number: 9876543210\n"
