import csv
from datetime import datetime   
#parser class
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
        print(len(self.data_books))
        print(self.head_books)
        print(head_size_books)
    
    def parse_person(self):
        with open(self.filename_person) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for line in csv_data:
                if line_count == 0:
                    #Things can be implemented later here such as more options for users data. but for now keeping it simple, will change later
                    line_count +=1
                else:
                    #As stated above, same thing for now keeping it name and username
                    self.data_person.append(person(line[0],line[1]))
        #debug
        print(len(self.data_person))

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
        print(self.data)

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
        s = f"\tTitle: {self.data[4]}\n\tISBN: {self.data[3]}\n\tAuther: {self.data[6]}\n"
        return s


class person:

    def __init__(self, name, username):
        self.name = name
        self.username = username

# class data:

#     def __init__(self, id, username):
#         self.id = int(id)
#         self.username = username
     

# def r_data(filename):
#     with open(filename, mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         line_count = 0
#         for line in csv_data:
#             if line_count == 0:
#                  line_count +=1
#             else:
#               pass

def takeout(object, id, username, filename):
    #TODO: Implement a check if the book was already taken out
    datenow = datetime.now()
    with open(filename, mode='a+') as csv_file:
        csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_data.writerow([id,username,str(datenow)])
    print(f"\n{username} has taken out the following book:\n{object.data_books[id]}")


    
a = parse_data("/Users/ahmad/Desktop/Projects/Simple-Library-Software/Books.csv", "/Users/ahmad/Desktop/Projects/Simple-Library-Software/users.csv", "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv")
a.parse_books()
a.parse_person()
a.parse_data()

takeout(a,11,"ahmad", "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv")


#TODO: 
    # Implement user search
    # Implement book search
    # Implement userids
    # switch statement possibly until GUI is ready