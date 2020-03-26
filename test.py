from classes import *
from datafunc import *
from main_func import *

filename_book = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/Books.csv"
filename_person = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/users.csv"
filename_data = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
filename = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
    
a = parse_data(filename_book, filename_person, filename_data)
a.parse_books()
a.parse_person()
a.parse_data()

# takeout(a,13,15, filename)
# user_search_id(a, 15, filename)
# username_search(a, "test", filename)

flag = True
print("Simple Library Software\n")
while flag == True:
    print("Please enter help or h for help")
    key1 = input("Input a command: ")
    key1 = key1.lower()
    if key1 == "h" or key1 == "help":
        print("Commands:\n\tt or takeout - To sign out a book\n\tr or return - To sign in a book\n\tu or user - To search up a user\n\tq or quit - To quit the program\n\tb or book - To search books\n")
    elif key1 == "q" or key1 == "quit":
        print("GoodBye!")
        flag = False
    elif key1 == "r" or key1 == "return":
        key1 = input("Would you like to use the student's username or id?: ")
        key1 = key1.lower()
        if key1 == "username":
            username = input("Please enter the student's username: ")
            id = None
            for i in a.data_person:
                if i.username == username:
                    id = i.pID
            if id == None:
                print("ERROR: Username NOT found!")
            else:
                bringtype = input("Would you like to use ISBN or the ID?: ")
                bringtype = bringtype.lower()
                if bringtype == "id":
                    bringid = input("Input the ID: ")
                    bringid = int(bringid)
                    bringback(a,int(bringid),int(id),filename)
                elif bringtype == "isbn":
                    bringisbn = input("Input the ISBN: ")
                    bringisbn = int(bringisbn)
                    bringid = None
                    for i in a.data_books:
                        if len(i.data[3]) == 0:
                            continue
                        if int(i.data[3]) == bringisbn:
                            bringid = int(i.data[0])
                    if bringid == None:
                        print("Book not found")
                    else:
                        bringback(a,int(bringid),int(id),filename)
        if key1 == "id":
            id = input("Please enter the student's ID: ")
            id = int(id)
            if id > len(a.data_person):
                print("ERROR: ID NOT found!")
            else:
                bringtype = input("Would you like to use ISBN or the ID?: ")
                bringtype = bringtype.lower()
                if bringtype == "id":
                    bringid = input("Input the ID: ")
                    bringid = int(bringid)
                    bringback(a,int(bringid),int(id),filename)
                elif bringtype == "isbn":
                    bringisbn = input("Input the ISBN: ")
                    bringisbn = int(bringisbn)
                    bringid = None
                    for i in a.data_books:
                        if len(i.data[3]) == 0:
                            continue
                        elif int(i.data[3]) == bringisbn:
                            bringid = int(i.data[0])
                    if bringid == None:
                        print("Book not found")
                    else:
                        bringback(a,int(bringid),int(id),filename)
    elif key1 == "t" or key1 == "takeout":
        key1 = input("Would you like to use the student's username or id?: ")
        key1 = key1.lower()
        if key1 == "username":
            username = input("Please enter the student's username: ")
            id = None
            for i in a.data_person:
                if i.username == username:
                    id = i.pID
            if id == None:
                print("ERROR: Username NOT found!")
            else:
                bringtype = input("Would you like to use ISBN or the ID?: ")
                bringtype = bringtype.lower()
                if bringtype == "id":
                    bringid = input("Input the ID: ")
                    bringid = int(bringid)
                    takeout(a,int(bringid),int(id),filename)
                elif bringtype == "isbn":
                    bringisbn = input("Input the ISBN: ")
                    bringisbn = int(bringisbn)
                    bringid = None
                    for i in a.data_books:
                        if len(i.data[3]) == 0:
                            continue
                        if int(i.data[3]) == bringisbn:
                            bringid = int(i.data[0])
                    if bringid == None:
                        print("Book not found")
                    else:
                        takeout(a,int(bringid),int(id),filename)
        if key1 == "id":
            id = input("Please enter the student's ID: ")
            id = int(id)
            if id > len(a.data_person):
                print("ERROR: ID NOT found!")
            else:
                bringtype = input("Would you like to use ISBN or the ID?: ")
                bringtype = bringtype.lower()
                if bringtype == "id":
                    bringid = input("Input the ID: ")
                    bringid = int(bringid)
                    takeout(a,int(bringid),int(id),filename)
                elif bringtype == "isbn":
                    bringisbn = input("Input the ISBN: ")
                    bringisbn = int(bringisbn)
                    bringid = None
                    for i in a.data_books:
                        if len(i.data[3]) == 0:
                            continue
                        elif int(i.data[3]) == bringisbn:
                            bringid = int(i.data[0])
                    if bringid == None:
                        print("Book not found")
                    else:
                        takeout(a,int(bringid),int(id),filename)
    elif key1 == "u" or key1 == "user":
        key1 = input("Would you like to use the student's username or id?: ")
        key1 = key1.lower()
        if key1 == "username":
            username = input("Please enter the student's username: ")
            username_search(a, username, filename)
        elif key1 == "id":
            id = input("Please enter the student's ID: ")
            user_search_id(a, int(id), filename)
    elif key1 == "b" or key1 == "book":
        title = input("Please enter the title, or part of the title: ")
        list_books = book_search(a,title)
        for i in list_books:
            print(i)



#TODO: 
    # Implement in main func
    # Implement due dates, with email system
    # Start slowly implementing GUI
