from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

from classes import *
from datafunc import *
from userdialog import *


class Ui_MainWindow(object):
    def __init__(self,data_books, data_person, data, filename, due, object):
        super().__init__() 
        self.data_books = data_books
        self.data_person = data_person
        self.data = data
        self.filename = filename
        self.object = object
        self.due = due
        self.userlist = self.data_person
        
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1353, 937)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 1271, 441))
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
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 540, 681, 331))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 820, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 71, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 510, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 510, 281, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(930, 610, 281, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(930, 540, 281, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 680, 281, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1353, 22))
        self.menubar.setObjectName("menubar")
        self.menuLibrary = QtWidgets.QMenu(self.menubar)
        self.menuLibrary.setObjectName("menuLibrary")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLibrary.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.itemDoubleClicked.connect(self.bookclick)
        self.tableWidget_2.itemDoubleClicked.connect(self.personclick)
        self.lineEdit.textChanged.connect(self.book_search)
        self.lineEdit_2.textChanged.connect(self.user_search)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.populatebooks()
        self.populateperson()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management Software"))
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
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Search:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Add User"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Book"))
        self.pushButton_4.setText(_translate("MainWindow", "Books Signed Out"))
        self.menuLibrary.setTitle(_translate("MainWindow", "Library"))


        
     
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
            event.buttons() == QtCore.Qt.RightButton and
            source is self.tblBoxes.viewport()):
            item = self.tblBoxes.itemAt(event.pos())
            if item is not None:
                print('dblclick:', item.row(), item.column())
        return super(MainWindow, self).eventFilter(source, event)

    def populatebooks(self):
        row = len(self.data_books)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(6)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        

        for i in range(row):
            #Change later to standerize csv file
            # self.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 0,QTableWidgetItem(self.data_books[i].data[0]))
            self.tableWidget.setItem(i, 1,QTableWidgetItem(self.data_books[i].data[4]))
            self.tableWidget.setItem(i, 2,QTableWidgetItem(self.data_books[i].data[6]))
            self.tableWidget.setItem(i, 3,QTableWidgetItem(self.data_books[i].data[15]))
            self.tableWidget.setItem(i, 4,QTableWidgetItem(self.data_books[i].data[3]))
            for j in self.data:
                if int(j[0]) == i:
                    self.tableWidget.setItem(i, 5,QTableWidgetItem("Signed Out"))
    
    def bookclick(self, item):
        print(item.row())

    def personclick(self, item):
        # pID = int(item.row())
        pID = int(self.userlist[item.row()].data[0])
        # import sys
        # app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.personui = Ui_Dialog(pID, self.data_books, self.data_person, self.data, self.filename,self.due, self.object)
        self.personui.setupUi(self.Dialog)
        self.Dialog.show()
        # sys.exit(app.exec_())
    #Investigate LAGGGGGGGGGGGGGGGGGGG
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
                if bookname.lower() in i.data[4].lower():
                    books.append(i)
            row = len(books)
            self.tableWidget.setRowCount(row)
            self.tableWidget.setColumnCount(6)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            

            for i in range(row):
                #Change later to standerize csv file
                # self.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 0,QTableWidgetItem(books[i].data[0]))
                self.tableWidget.setItem(i, 1,QTableWidgetItem(books[i].data[4]))
                self.tableWidget.setItem(i, 2,QTableWidgetItem(books[i].data[6]))
                self.tableWidget.setItem(i, 3,QTableWidgetItem(books[i].data[15]))
                self.tableWidget.setItem(i, 4,QTableWidgetItem(books[i].data[3]))
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
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#         self.populatebooks()
#         self.populateperson()







