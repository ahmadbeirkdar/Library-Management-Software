import sys
sys.path.append('gui')
from mainwindow import *
from userdialog import *
from classes import *
from datafunc import *
from bookadd import *


filename_book = "books.csv"
filename_person = "users.csv"
filename_data = "data.csv"
filename = "data.csv"
duetime = 14

a = parse_data(filename_book, filename_person, filename_data)
a.parse_books()
a.parse_person()
a.parse_data()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(filename, duetime, a)
ui.setupUi(MainWindow)

MainWindow.show()

sys.exit(app.exec_())

#NOTE:
    # Col 1 ID, Col 2 Title, Col 3 Author, Col 4 ISBN, Col 5 Location

#TODO:
    # Implement bring back books -DONE
    # Book add - DONE
        # Implement book csv standared - Done
        # csv append - DONE
    # Loging system - DONE
    # Implement settings
        # default thingss
    # Implement books due
        # Email
        # Due books list
    # Implement Dues system
        # csv
    # Refresh main window for added books and data
    # Add user functionality 




