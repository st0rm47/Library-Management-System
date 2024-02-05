from library import Library
from library import Book
from library import Member


#Main Function
def main():
    #Creating a list of books and members
    library = Library()
    
    # switch case options for adding/removing books, adding/removing members, 
    # borrowing/returning books and displaying books/members
    while 1:
        print("\nLibrary Management System")
        print("=========================")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Display Books")
        print("8. Display Members")
        print("9. Exit")
        
        option = int(input("\nEnter the option: \n"))
        match option:
            case 1:
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                ISBN = input("Enter the ISBN number of the book: ")
                availability = input("Enter the availability of the book(True/False): ")                
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