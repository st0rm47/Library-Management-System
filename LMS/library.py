#Library Management System

#Book Class
class Book:
    #Constructor
    def __init__(self,title,author,ISBN,availability):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
            
    #Method to mark book as borrowed or returned
    def borrow_book(self):
        self.availability = False
    
    def return_book(self):
        self.availability = True
        
    #Method to display the data of the book
    def display_book(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("ISBN: ", self.ISBN)
        print("Availability: ", "Available" if self.availability else "Not Available")
    
#Member Class
class Member:
    #Constructor
    def __init__(self,name,member_id,phone_number):
        self.name = name
        self.member_id = member_id
        self.phone_number = phone_number
    
    #Method to display the data of the member
    def display_member(self):
        print("Name: ", self.name)
        print("Member ID: ", self.member_id)
        print("Phone Number: ", self.phone_number)
        
#Library Class 
class Library:
    #Constructor
    def __init__(self):
        self.books = []
        self.members = []
    
    #Method to add a book to the library
    def add_book(self,book):
        self.books.append(book)
    
    #Method to remove a book from the library using the ISBN
    def remove_book(self,ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"{book.title} Removed")
                break
            else:
                print(f"{book.title} not found")    
        
    #Method to add new member to the library
    def add_member(self,member):
        self.members.append(member)
    
    #Method to remove a member from the library using the member id
    def remove_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"{member.name} Removed")
                break
            else:
                print(f"{member.name} not found") 
                
    #Method to allow a member to borrow a book using member id and ISBN number checking the availability of the book
    def borrow_book(self,member_id,ISBN):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.ISBN == ISBN:
                        if book.availability:
                            book.borrow_book()
                            print(f"{member.name} borrowed {book.title}")
                            break
                        else:
                            print(f"{book.title} is not Available")
                            break
                    else:
                        print("Book not found")
            else:
                print("Member not found")
        
    #Method to allow a member to return a book using member id and ISBN number
    def return_book(self,member_id,ISBN):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.ISBN == ISBN:
                        if not book.availability:
                            book.return_book()
                            print(f"{member.name} returned {book.title}")
                            break
                        else:
                            print(f"{book.title} is not Borrowed")
                            break
                    else:
                        print("Book not found")
            else:
                print("Member not found")
    
    #Method to display all books of Library
    def display_book(self):
        for book in self.books:
            book.display_book()
    
    #Method to display all members of Library
    def display_member(self):
        for member in self.members:
            member.display_member()

