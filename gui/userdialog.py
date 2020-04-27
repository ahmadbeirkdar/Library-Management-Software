from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QDialog, QMessageBox, QAction, QWidget, QInputDialog
from classes import *
from datafunc import *
from functools import partial



class Ui_Dialog(QWidget):
    def __init__(self, id,data_books, data_person, data, filename, due, object):
        super().__init__()
        self.id = id
        self.data_books = data_books
        self.data_person = data_person
        self.data = data
        self.filename = filename
        self.due = due
        self.object = object
        self.books = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 596)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 320, 591, 231))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 280, 311, 31))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 60, 341, 181))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 311, 31))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 100, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 160, 171, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 140, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 80, 58, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 190, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 560, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
    

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.Signout)
        self.pushButton_2.clicked.connect(Dialog.accept)
        self.tableWidget.doubleClicked.connect(self.ask)
     
        self.populateuser()
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Information"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Title"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ISBN"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Signed Out"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Due"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; text-decoration: underline;\">Books Signed Out:</span></p></body></html>"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Username"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Email"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Dues"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; text-decoration: underline;\">User Information:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "ISBN"))
        self.label_4.setText(_translate("Dialog", "ID"))
        self.pushButton.setText(_translate("Dialog", "Sign Out"))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))

    
    def Signout(self):
        Bid = self.lineEdit.text()
        isbn = self.lineEdit_2.text()
        if len(Bid) > 0:
            if int(Bid) < len(self.data_books):
                s = takeout(self.object,int(Bid), self.id, self.due,self.filename)
                self.populateuser()
                msg = QMessageBox()
                msg.setWindowTitle("Library")
                msg.setText(s)
                x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Library")
                msg.setText("ERROR: YOU LIKELY ENTERED AN OUT OF RANGE BOOK ID")
                x = msg.exec_()
        elif len(isbn) > 0:
            bringisbn = int(isbn)
            bringid = None
            for i in self.data_books:
                if len(i.isbn) == 0:
                    continue
                if int(i.isbn) == bringisbn:
                    bringid = int(i.id)
            if bringid == None:
                s = "Book Not Found"
            
            else:
                s = takeout(self.object,int(bringid),self.id, self.due,self.filename)
                self.populateuser()
            msg = QMessageBox()
            msg.setWindowTitle("Library")
            msg.setText(s)
            x = msg.exec_()
    
    def ask(self, item):
        bookid = int(self.books[item.row()])
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Prompt")
        msgbox.setText('Would you like to?')
        msgbox.addButton(QMessageBox.Cancel)
        msgbox.addButton('Return', QMessageBox.YesRole)
        msgbox.addButton('Extend', QMessageBox.NoRole)
        retval = msgbox.exec_()

        if retval == 0:
            s = bringback(self.object,bookid,self.id,self.filename)

            self.populateuser()
            msg = QMessageBox()
            msg.setWindowTitle("Library")
            msg.setText(s)
            x = msg.exec_()
        if retval == 1:
            day, ok  = QInputDialog.getText(self, 'Library', 'Enter the amount of days to extend:')
            if len(day) > 0:
                s = extend(self.object,int(bookid), int(self.id),int(day),self.filename)
                self.populateuser()
                msg = QMessageBox()
                msg.setWindowTitle("Library")
                msg.setText(s)
                x = msg.exec_()

    def populateuser(self):
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(1)
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #IMPLMENT DUES LATER
        for i in range(0,4):
            self.tableWidget_2.setItem(i, 0,QTableWidgetItem(self.data_person[self.id].data[i]))

        self.data  = read_data(self.filename)
        self.books = []
        dates = []
        duedate = []

        for i in self.data:
            if int(i[1]) == self.id:
                self.books.append(i[0])
                dates.append(i[2])
                duedate.append(i[3])

        if len(self.books) > 0:
            self.tableWidget.setRowCount(len(self.books))
            self.tableWidget.setColumnCount(5)
            header1 = self.tableWidget.horizontalHeader()
            header1.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header1.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header1.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header1.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header1.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

            for i in range(len(self.books)):
                self.tableWidget.setItem(i, 0,QTableWidgetItem(self.books[i]))
                self.tableWidget.setItem(i, 1,QTableWidgetItem(self.data_books[int(self.books[i])].title))
                self.tableWidget.setItem(i, 2,QTableWidgetItem(self.data_books[int(self.books[i])].isbn))
                self.tableWidget.setItem(i, 3,QTableWidgetItem(dates[i]))
                self.tableWidget.setItem(i,4,QTableWidgetItem(duedate[i]))

        elif len(self.books) == 0:
            self.tableWidget.setRowCount(0)