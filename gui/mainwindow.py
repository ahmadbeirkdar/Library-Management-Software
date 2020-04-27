from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QMessageBox

from classes import *
from datafunc import *
from userdialog import *
from bookadd import *


class Ui_MainWindow(object):
    def __init__(self,filename, due, object):
        super().__init__() 
        self.data_books = object.data_books
        self.data_person = object.data_person
        self.data = object.data
        self.filename = filename
        self.object = object
        self.due = due
        self.userlist = self.data_person

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 984)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMouseTracking(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget_2, 3, 0, 1, 5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 22))
        self.menubar.setObjectName("menubar")
        self.menuLibrary = QtWidgets.QMenu(self.menubar)
        self.menuLibrary.setObjectName("menuLibrary")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLibrary.menuAction())

        self.tableWidget.itemDoubleClicked.connect(self.bookclick)
        self.tableWidget_2.itemDoubleClicked.connect(self.personclick)
        self.lineEdit.textChanged.connect(self.book_search)
        self.lineEdit_2.textChanged.connect(self.user_search)
        self.pushButton_3.clicked.connect(self.book_add)
        self.populatebooks()
        self.populateperson()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management Software"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Book Search:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">User Search:</span></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.pushButton_4.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Book"))
        self.pushButton_5.setText(_translate("MainWindow", "Settings"))
        self.pushButton_6.setText(_translate("MainWindow", "Add User"))
        self.menuLibrary.setTitle(_translate("MainWindow", "Library"))



    def populatebooks(self):
        row = len(self.data_books)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(6)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        
        for i in range(row):
            self.tableWidget.setItem(i, 0,QTableWidgetItem(self.data_books[i].id))
            self.tableWidget.setItem(i, 1,QTableWidgetItem(self.data_books[i].title))
            self.tableWidget.setItem(i, 2,QTableWidgetItem(self.data_books[i].author))
            self.tableWidget.setItem(i, 3,QTableWidgetItem(self.data_books[i].location))
            self.tableWidget.setItem(i, 4,QTableWidgetItem(self.data_books[i].isbn))
            for j in self.data:
                if int(j[0]) == i:
                    self.tableWidget.setItem(i, 5,QTableWidgetItem("Signed Out"))
    
    def bookclick(self, item):
        print(item.row())
        # self.object.parse_data()
        # self.object.parse_books()
        # self.data = self.object.data
        # self.data_books = self.object.data_books
        # self.populatebooks()

    def personclick(self, item):
        pID = int(self.userlist[item.row()].data[0])
        self.Dialog = QtWidgets.QDialog()
        self.personui = Ui_Dialog(pID, self.data_books, self.data_person, self.data, self.filename,self.due, self.object)
        self.personui.setupUi(self.Dialog)
        self.Dialog.show()
    
    def book_add(self,item):
        self.Dialog2 = QtWidgets.QDialog()
        self.bookui = Ui_Dialog_bookadd(self.object,self)
        self.bookui.setupUi(self.Dialog2)
        self.Dialog2.show()
        
    def user_search(self):
        username = self.lineEdit_2.text()
        if len(username) > 0:
            self.userlist = []
            for i in self.data_person:
                if username.lower() in i.data[1].lower():
                    self.userlist.append(i)
            row = len(self.userlist)
            self.tableWidget_2.setRowCount(row)
            self.tableWidget_2.setColumnCount(4)
            header = self.tableWidget_2.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            
            for i in range(row):
                self.tableWidget_2.setItem(i, 0,QTableWidgetItem(self.userlist[i].data[0]))
                self.tableWidget_2.setItem(i, 1,QTableWidgetItem(self.userlist[i].data[1]))
                self.tableWidget_2.setItem(i, 2,QTableWidgetItem(self.userlist[i].data[2]))
                self.tableWidget_2.setItem(i, 3,QTableWidgetItem(self.userlist[i].data[3]))
        else:
            self.userlist = self.data_person
            self.populateperson()
        
    def book_search(self):
        books =[]
        bookname = self.lineEdit.text()

        if len(bookname) > 0:
            for i in self.data_books:
                if bookname.lower() in i.title.lower():
                    books.append(i)

            row = len(books)
            self.tableWidget.setRowCount(row)
            self.tableWidget.setColumnCount(6)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            
            for i in range(row):
                self.tableWidget.setItem(i, 0,QTableWidgetItem(books[i].id))
                self.tableWidget.setItem(i, 1,QTableWidgetItem(books[i].title))
                self.tableWidget.setItem(i, 2,QTableWidgetItem(books[i].author))
                self.tableWidget.setItem(i, 3,QTableWidgetItem(books[i].isbn))
                self.tableWidget.setItem(i, 4,QTableWidgetItem(books[i].location))
                for j in self.data:
                    if int(j[0]) == i:
                        self.tableWidget.setItem(i, 5,QTableWidgetItem("Signed Out"))
        else:
            self.populatebooks()

    def populateperson(self):
        row = len(self.data_person)
        self.tableWidget_2.setRowCount(row)
        self.tableWidget_2.setColumnCount(4)
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        
        for i in range(row):
            for j in range(4):
                self.tableWidget_2.setItem(i, j,QTableWidgetItem(self.data_person[i].data[j]))
            
        




# self.tableWidget.itemDoubleClicked.connect(self.bookclick)
#         self.tableWidget_2.itemDoubleClicked.connect(self.personclick)
#         self.lineEdit.textChanged.connect(self.book_search)
#         self.lineEdit_2.textChanged.connect(self.user_search)
#         self.pushButton_3.clicked.connect(self.book_add)
#         self.populatebooks()
#         self.populateperson()
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)


