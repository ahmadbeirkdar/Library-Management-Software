import csv
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
                    #Things can be implemented later here such as more options for users data. but for now keeping it simple, will change later
                    line_count +=1
                else:
                    #As stated above, same thing for now keeping it name and username and ID
                    self.data_person.append(person(line[0],line[1], line[2]))
        #debug
        # print(len(self.data_person))

    def parse_data(self):
        with open(self.filename_data) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in csv_data:
                if line_count == 0:
                     line_count +=1
                else:
                    self.data.append(line)
        #debug
        # print(self.data)

#Book Data Class
class book_data():

    def __init__(self, data):
        self.data = data

    def addcell(self):
        for i in self.data:
            self.list1.append(i)
    
    def title(self):
        return self.data[4]

    # def __str__(self):
    #     s = ' '.join([str(i) for i in self.data])
    #     s = s+"\n"
    #     return s
    def __str__(self):
        s = f"\tTitle: {self.data[4]}\n\tISBN: {self.data[3]}\n\tAuthor: {self.data[6]}\n"
        return s


class person:
    def __init__(self, pID, name, username):
        self.name = name
        self.username = username
        self.pID = pID
