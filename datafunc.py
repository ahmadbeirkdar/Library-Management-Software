import csv
from datetime import datetime, timedelta

def read_data(filename):
    data =[]
    with open(filename) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        for line in csv_data:
            data.append(line)
    return data

# def takeout(object, id, pid, due, filename):
#     data = read_data(filename)
#     flag = True
#     for i in data:
#         if int(i[0]) == id:
#             print(f"ERROR: The following book is already signed out by {object.data_person[int(i[1])].name} on the data {i[2]}")
#             flag = False
#             break
#     if len(data) == 0 or flag == True:
#         datenow = datetime.now().date()
#         duedate = datenow + timedelta(days=due)
#         with open(filename, mode='a+') as csv_file:
#             csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             csv_data.writerow([id,pid,str(datenow), str(duedate)])
#         print(f"\n{object.data_person[pid].name} has taken out the following book:\n{object.data_books[id]}")
def takeout(object, id, pid, due, filename):
    data = read_data(filename)
    flag = True
    s = " "
    for i in data:
        if int(i[0]) == id:
            s = f"ERROR: The following book is already signed out by {object.data_person[int(i[1])].name} on the date {i[2]}"
            log(s)
            return s
    if len(data) == 0 or flag == True:
        datenow = datetime.now().date()
        duedate = datenow + timedelta(days=due)
        with open(filename, mode='a+') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_data.writerow([id,pid,str(datenow), str(duedate)])
        s = f"\n{object.data_person[pid].name} has taken out the following book:\n{object.data_books[id]}"
        log(s)
        return s

def bringback(object,id,pid,filename):
    data = read_data(filename)
    flag = True
    for i in data:
        if int(i[0]) == id:
            flag = False
    if flag == True:
        s = (f"ERROR: The following book was not signed out!\n{object.data_books[id]}")
        log(s)
        return s
    else:
        for i in range(0,len(data)):
            if int(data[i][0]) == id:
                del data[i]
                break
        with open(filename, mode='w') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in data:
                csv_data.writerow(i)
        s = (f"\n{object.data_person[pid].name} has signed in the following book:\n{object.data_books[id]}")
        log(s)
        return s

def extend(object,id,pid, day,filename):
    data = read_data(filename)
    datenow = datetime.now().date()
    duedate = datenow + timedelta(days=day)
    flag = True
    for i in data:
        if int(i[0]) == id:
            flag = False
    if flag == True:
        s = (f"ERROR: The following book was not signed out!\n{object.data_books[id]}")
        log(s)
        return s
    else:
        for i in range(0,len(data)):
            if int(data[i][0]) == id:
                data[i] = [id,pid,str(datenow), str(duedate)]
                break
        with open(filename, mode='w') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in data:
                csv_data.writerow(i)
        s = (f"\n{object.data_person[pid].name} has extended by {day} days the following book:\n{object.data_books[id]}")
        log(s)
        return s
        
def user_search_id(object, id, filename):
    id = int(id)
    data = read_data(filename)
    books = []
    dates = []
    duedate = []
    for i in data:
        if int(i[1]) == id:
            books.append(object.data_books[int(i[0])])
            dates.append(i[2])
            duedate.append(i[3])
    if len(books) == 0:
        print("No loans under this account")
    else:
        print(f"\n{object.data_person[id].name} has the following books out: ")
        j = 0
        for i in books:
            print(i)
            print(f"\tSigned out: {dates[j]}")
            print(f"\tDue on: {duedate[j]}\n")
            j += 1

def username_search(object, username, filename):
    data = read_data(filename)
    books = []
    dates = []
    id = None
    for i in object.data_person:
        if str(i.username) == str(username):
            id = int(i.pID)
    if id != None:
        for i in data:
            if int(i[1]) == id:
                books.append(object.data_books[int(i[0])])
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

def book_search(object, bookname):
    books =[]
    for i in object.data_books:
        if bookname.lower() in i.title.lower():
            books.append(i)
    return books

def log(logs):
    f = open("LMS.log", "a")
    datenow = datetime.now()
    f.write(f"\nOn {datenow} the following took place:\n\t{logs}\n")
    f.close()

def sendemail(object,Remail,Semail,EmailPass, userid, bookid, date):
    import smtplib, ssl
    from email.message import EmailMessage
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = Semail
    password = EmailPass
    

    msg = EmailMessage()
    msg.set_content(f"Hello {object.data_person[userid].name}, \nThe following book is due on {date}:\n{object.data_books[bookid]}")

    msg['Subject'] = f'{object.data_books[bookid].title} is due!'
    msg['From'] = Semail
    msg['To'] = Remail

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(Semail, password)
    server.send_message(msg)
    server.quit()
   


