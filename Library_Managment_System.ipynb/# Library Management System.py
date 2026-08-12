# Library Management System 
print("=============LIBRARY MANAGEMENT SYSTEM===============\n"
    "1. Add book to library\n"
    "2. Update book to library\n"
    "3. Delete book\n"
    "4. Return book\n"
    "5. Display available books\n"
    "6. Display issued books\n"
    "7. Issue book\n"
     )
#input the operation to perform
try :
    todo = (int(input("Choose an option from above:")))
    
    # books in library
    books_available = [
        [102, "The Alchemist", "Paulo Coelho"],
        [103, "Harry Potter and the Philosopher's Stone", "J.K. Rowling"],
        [104, "To Kill a Mockingbird", "Harper Lee"],
        [106, "The Great Gatsby", "F. Scott Fitzgerald"],
        [107, "Pride and Prejudice", "Jane Austen"],
        [109, "The Hobbit", "J.R.R. Tolkien"],
        [110, "The Catcher in the Rye", "J.D. Salinger"],
        [111, "1984", "George Orwell"],
        [115, "The Kite Runner", "Khaled Hosseini"],
        [116, "Wings of Fire", "A.P.J. Abdul Kalam"]
        ]
    #issued books list for library
    books_issued = [
        [101, "The Da Vinci Code", "Dan Brown"],
        [105, "The Fault in Our Stars", "John Green"],
        [108, "The Hunger Games", "Suzanne Collins"],
        [112, "Life of Pi", "Yann Martel"],
        [113, "The Book Thief", "Markus Zusak"],
        [114, "The Chronicles of Narnia", "C.S. Lewis"],
        [117, "The Little Prince", "Antoine de Saint-Exupery"],
        [118, "Animal Farm", "George Orwell"],
        [119, "The Secret", "Rhonda Byrne"],
        [120, "The Power of Habit", "Charles Duhigg"]
        ]
    #Add book to library
    if todo == 1:
        new_book = []
        book_id1 = int(input("Enter the book ID:"))
        found = False
        for book in books_available:
            if book[0] == book_id1:
                found = True
                break
        for book in books_issued:
            if book[0] == book_id1:
                found = True
                break  
        if found:
            print("The Book ID is already in the library")
        else:
            book_title1 = input("Enter the book title:")
            book_author1 = input("Enter the book author name:")   
            new_book=[book_id1,book_title1,book_author1]
            books_available.append(new_book)
            books_available.sort()
            print("Book added successfully")
        for book in books_available:
            print("Book ID:",book[0])
            print("Book Name:",book[1])
            print("Book Author:",book[2])
            print("-"*30)
            
    # Update the list change name and author details
    elif todo == 2:
        print("What you want to update:\n"
             "1. Book ID\n"
             "2. Book Name\n"
             "3. Book author details\n")
        book_update = int(input("Choose an option that you want to update"))
        if 1<=book_update<=3: 
            book_id2 = int(input("Enter the Book ID you want to update"))
            for book in books_available:
                if book[0] == book_id2:
                    if book_update == 1:
                        new_id= int(input("Enter the new book ID"))
                        found = False
                        for book in books_available:
                            if book[0] == new_id:
                                found = True
                                break
                        for book in books_issued:
                            if book[0] == new_id:
                                found = True
                                break 
                        if found:
                            print("Entered Book ID is already in the library")
                        else:
                            for book in books_available:
                                if book[0] == book_id2:
                                    book[0] = new_id
                                    books_available.sort()
                                    print(books_available)
                                    break
                    elif book_update == 2:
                        new_name= input("Enter the new book name")
                        for book in books_available:
                            if book[0] == book_id2:
                                book[1] = new_name
                        books_available.sort()
                        print(books_available)
                        break
                    elif book_update == 3:
                        new_author= input("Enter the new author name")
                        for book in books_available:
                            if book[0] == book_id2:
                                book[2] = new_author
                        books_available.sort()
                        print(books_available)
                        break
                    else:
                        print("Enter a valid option")
        else:
            print("Entered option invalid")
    # To delete a book
    elif todo == 3:
        book_id3 = int(input("Enter the book ID:"))
        found = False
        for book in books_available:
            if book[0] == book_id3:
                found = True
                break
        if not found:
            print("Enter a valid id")
        else:
            for book in books_available:
                if book[0] == book_id3:
                    books_available.remove(book)
                    print(f"BookID {book_id3} deleted successfully")
                    for book in books_available:
                        print("Book ID:",book[0])
                        print("Book Name:",book[1])
                        print("Book Author:",book[2])
                        print("-"*30)
                    break
    # To return the book
    elif todo == 4:
        book_id4 = int(input("Enter the book ID:"))
        for book in books_issued:
            if book[0] == book_id4:
                books_issued.remove(book)
                print("Issued book list:\n",books_issued)
                books_available.append(book)
                books_available.sort()
                print("Available book list:\n" ,books_available)
                break
        else:
            print("Entered ID not found in issued books")
    #Display the list of available books
    elif todo == 5:
        for book in books_available:
            print("Book ID:",book[0])
            print("Book Name:",book[1])
            print("Book Author:",book[2])
            print("-"*30)

    #Display the list of issued books
    elif todo ==6:
        for book in books_issued:
            print("Book ID:",book[0])
            print("Book Name:",book[1])
            print("Book Author:",book[2])
            print("-"*30)
    
    #Issue books
    elif todo == 7:
        book_id7 = int(input("Enter the book ID you want to issue:"))
        found = False
        for book in books_available:
            if book[0] == book_id7:
                books_available.remove(book)
                books_issued.append(book)
                books_issued.sort()
                found = True
                print(f"Book ID {book_id7} is issued")
                print("Display the list of issued books:\n",books_issued)
                print("Display the list of available books:\n",books_available)
                break
        if not found:
            print("Please enter a valid Book ID")
    else:
        print("Enter a number between 1 to 7")
except ValueError:
    print("Enter a valid input")
finally:
    print("Thank you")
        

