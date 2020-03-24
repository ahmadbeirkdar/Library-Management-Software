from classes import *
from datafunc import *

filename_book = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/Books.csv"
filename_person = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/users.csv"
filename_data = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
filename = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
    
a = parse_data(filename_book, filename_person, filename_data)
a.parse_books()
a.parse_person()
a.parse_data()

takeout(a,13,15, filename)
user_search_id(a, 15, filename)
# username_search(a, "test", filename)



#TODO: 
    # Implement book search
    # switch statement possibly until GUI is ready