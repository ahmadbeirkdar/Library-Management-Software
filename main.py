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
        pass
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
    





#TODO: 
    # Implement book search
    # switch statement possibly until GUI is ready
    # Implement in main func