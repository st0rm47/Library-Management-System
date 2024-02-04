
#Book Class
class Book:
    #Constructor
    def __init__(self,title,author,ISBN,availability):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
    
    # #Method to initialize the book
    # def initialize_book(self, title, author, ISBN, availability):
    #     self.title = title
    #     self.author = author
    #     self.ISBN = ISBN
    #     self.availability = availability
        
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
        if self.availability == True:
            print("Availability: Available")
        else:
            print("Availability: Borrowed")  
    

#Member Class
class Member:
    #Constructor
    def __init__(self,name,member_id,phone_number):
        self.name = name
        self.member_id = member_id
        self.phone_number = phone_number
    
    # #Method to initialize the member
    # def initialize_member(self, name, member_id, phone_number):
    #     self.name = name
    #     self.member_id = member_id
    #     self.phone_number = phone_number
    
    #Method to display the data of the member
    def display_member(self):
        print("Name: ", self.name)
        print("Member ID: ", self.member_id)
        print("Phone Number: ", self.phone_number)
        
#Library Class 
class Library:
    #Constructor
    def __init__(self,books,members):
        self.books = books
        self.members = members
    
    #Method to add a book to the library
    def add_book(self,book):
        self.books.append(book)
    
    #Method to remove a book from the library using the ISBN
    def remove_book(self,ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print("Book Removed")
        print("Book not found")    
        
    #Method to add new member to the library
    def add_member(self,member):
        self.members.append(member)
    
    #Method to remove a member from the library using the member id
    def remove_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print("Member Removed")
        print("Member not found") 
                
    #Method to allow a member to borrow a book using member id and ISBN number checking the availability of the book
    def borrow_book(self,member_id,ISBN):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.ISBN == ISBN:
                        if book.availability == True:
                            book.borrow_book()
                            print("Book is Borrowed")
                        else:
                            print("Book is not Available")
                print("Book not found")
        print("Member not found")
        
    #Method to allow a member to return a book using member id and ISBN number
    def return_book(self,member_id,ISBN):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.ISBN == ISBN:
                        if book.availability == False:
                            book.return_book()
                            print("Book is Returned")
                        else:
                            print("Book is not Borrowed")
                print("Book not found")
        print("Member not found")
    
    #Method to display all books of Library
    def display_book(self):
        for book in self.books:
            book.display_book()
    
    #Method to display all members of Library
    def display_member(self):
        for member in self.members:
            member.display_member()

#Main Function
def main():
    #Creating a list of books and members
    books = []
    members = []
    
    # switch case options for adding/removing books, adding/removing members, 
    # borrowing/returning books and displaying books/members
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Add Member")
    print("4. Remove Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Books")
    print("8. Display Members")
    print("9. Exit")
    
    #Creating a library object
    library = Library(books,members)
    
    #To keep running until the user exits
    while 1:
        option = int(input("Enter the option: "))
        match option:
            case 1:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                ISBN = input("Enter the ISBN number of the book: ")
                availability = input("Enter the availability of the book: ")                
                book = Book(title,author,ISBN,availability)
                library.add_book(book)
            case 2:
                ISBN = input("Enter the ISBN of the book: ")
                library.remove_book(ISBN)
            case 3:
                name = input("Enter the name of the member: ")
                member_id = input("Enter the member id of the member: ")
                phone_number = input("Enter the phone number of the member: ")
                member = Member(name,member_id,phone_number)
                library.add_member(member)
            case 4:
                member_id = input("Enter the member id of the member: ")
                library.remove_member(member_id)
            case 5:
                member_id = input("Enter the member id of the member: ")
                ISBN = input("Enter the ISBN of the book: ")
                library.borrow_book(member_id,ISBN)
            case 6:
                member_id = input("Enter the member id of the member: ")
                ISBN = input("Enter the ISBN of the book: ")
                library.return_book(member_id,ISBN)
            case 7:
                library.display_book()
            case 8:
                library.display_member()
            case 9:
                break
            case _:
                print("Invalid Option")
                
#Calling the main function
if __name__ == "__main__":
    main()