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
        s = f"\tTitle: {self.data[4]}\n\tISBN: {self.data[3]}\n\tAuther: {self.data[6]}"
        return s


class person:
    def __init__(self, pID, name, username):
        self.name = name
        self.username = username
        self.pID = pID

def read_data(filename):
    data =[]
    with open(filename) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for line in csv_data:
            data.append(line)
    return data

def takeout(object, id, pid, filename):
    data = read_data(filename)
    flag = True
    for i in data:
        if int(i[0]) == id:
            print(f"ERROR: The following book is already signed out by {a.data_person[int(i[1])].name} on the data {i[2]}")
            flag = False
            break
    if len(data) == 0 or flag == True:
        datenow = datetime.now()
        with open(filename, mode='a+') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_data.writerow([id,pid,str(datenow)])
        print(f"\n{object.data_person[pid].name} has taken out the following book:\n{object.data_books[id]}")

def user_search_id(object, id, filename):
    id = int(id)
    data = read_data(filename)
    books = []
    dates = []
    for i in data:
        if int(i[1]) == id:
            books.append(a.data_books[int(i[0])])
            dates.append(i[2])
    if len(books) == 0:
        print("No loans under this account")
    else:
        print(f"\n{object.data_person[id].name} has the following books out: ")
        j = 0
        for i in books:
            print(i)
            print(f"\tOn: {dates[j]}\n")
            j += 1

def username_search(object, username, filename):
    data = read_data(filename)
    books = []
    dates = []
    id = None
    for i in a.data_person:
        if str(i.username) == str(username):
            id = int(i.pID)
    if id != None:
        for i in data:
            if int(i[1]) == id:
                books.append(a.data_books[int(i[0])])
                dates.append(i[2])
        if len(books) == 0:
            print("No loans under this account")
        else:
            print(f"\n{object.data_person[id].name} has the following books out: ")
            j = 0
            for i in books:
                print(i)
                print(f"\tOn: {dates[j]}\n")
                j += 1
    else:
        print("User not found")  

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



#TODO: 
    # Implement book search
    # switch statement possibly until GUI is ready