#classes >> Library and Customer
#Layers of abstraction for Library :: Display available books, lend a Book, add a Book
#Layers of abstraction for Customer :: Request for a book, Return a Book


class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks


    def displayAvailableBooks(self):
        print()
        print("Available Books::")
        for book in self.availableBooks:
            print(book)
            print()

    def lendABook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("you have now borrowed {}".format(requestedBook))
            self.availableBooks.remove(requestedBook)
            print()
        else:
            print("Sorry {} is not available in the library".format(requestedBook))
            print()

        

    def addABook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("Thank You, {} has be returned successfully".format(returnedBook))
        print()


class Customer:
    def requstForBook(self):
        print("Enter the book you want to borrow")
        self.book = input().upper()
        return self.book

    def returnABook(self):
        print("Please Enter the book you want to return")
        self.book = input().upper()
        return self.book


library = Library(["THINK AND GROW RICH", "RICH DAD AND POOR DAD", "THERE WAS A COUNTRY","WHO WILL CRY WHEN YOU DIE"])
customer = Customer()

while True:
    print("Enter 1 to Display the available Books")
    print("Enter 2 to Request a Book")
    print("Enter 3 to Return a Book")
    print("Enter 4 to Exit")

    userChoice = int(input())

    if userChoice == 1:
        library.displayAvailableBooks()

    elif userChoice == 2:
        requestedBook = customer.requstForBook()
        library.lendABook(requestedBook)

    elif userChoice == 3:
        returnedBook = customer.returnABook()
        library.addABook(returnedBook)

    elif userChoice == 4:
        quit()

