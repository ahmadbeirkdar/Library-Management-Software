import sys
sys.path.append('Simple-Library-Software/gui')
from mainwindow import *
from userdialog import *
from classes import *
from datafunc import *
from bookadd import *


filename_book = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/Books.csv"
filename_person = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/users.csv"
filename_data = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
filename = "/Users/ahmad/Desktop/Projects/Simple-Library-Software/data.csv"
duetime = 14
    
a = parse_data(filename_book, filename_person, filename_data)
a.parse_books()
a.parse_person()
a.parse_data()


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(a.data_books,a.data_person,a.data,filename, duetime, a)
ui.setupUi(MainWindow)

MainWindow.show()


sys.exit(app.exec_())

#NOTE:
    # Col 1 ID, Col 2 Title, Col 3 Author, Col 4 ISBN, Col 5 Location

#TODO:
    #Implement bring back books
    # Book add
        # Implement book csv standared
        