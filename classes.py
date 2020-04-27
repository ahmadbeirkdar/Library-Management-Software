import csv
from datafunc import *
from datetime import datetime 
class parse_data():

    def __init__(self, filename_book, filename_person, filename_data):
        self.filename_book = filename_book
        self.filename_person = filename_person
        self.filename_data = filename_data
        self.head_books = []
        self.data_books = []
        self.head_person = []
        self.data_person =[]
        self.data = []
        
    def parse_books(self):
        with open(self.filename_book) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            line_count = 0
            head_size = 0
            for line in csv_data:
                if line_count == 0:
                    self.head_books = line
                    head_size_books = len(self.head_books)
                    line_count +=1
                else:
                    self.data_books.append(book_data(line))
        #debug
        # print(len(self.data_books))
        # print(self.head_books)
        # print(head_size_books)
    
    def parse_person(self):
        with open(self.filename_person) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in csv_data:
                if line_count == 0:
                    line_count +=1
                else:
                    self.data_person.append(person(line[0],line[1], line[2],line[3]))
        #debug
        # print(len(self.data_person))

    def parse_data(self):
        with open(self.filename_data) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in csv_data:
                    self.data.append(line)

        #debug
        # print(self.data)
    def addbook(self, title, author, isbn = None,location = None):
        data = [len(self.data_books),title,author, isbn,location]
        with open(self.filename_book, mode='a+') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_data.writerow(data)
        
        self.data_books.append(book_data(data))
        s = " "
        for i in data:
            s += " " + str(i)
        log(f"The following book was added {s}")




class book_data():

    def __init__(self, data):
        self.data = data
        self.id = data[0]
        self.title = data[1]
        self.author = data[2]
        self.isbn = data[3]
        self.location = data[4]

    def addcell(self):
        for i in self.data:
            self.list1.append(i)
    
    def __str__(self):
        s = f"\t\nTitle: {self.title}\n\tISBN: {self.isbn}\n\tAuthor: {self.author}"
        return s


class person:
    def __init__(self, pID, name, username, email):
        self.name = name
        self.username = username
        self.pID = pID
        self.email = email
        self.data = [pID,name,username,email]
