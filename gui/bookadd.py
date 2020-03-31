from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import isbnlib



from classes import *
from datafunc import *
from userdialog import *
from mainwindow import *

class Ui_Dialog_bookadd(object):
    def __init__(self, object,window):
        super().__init__()
        self.object = object
        self.window = window
        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 232)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 58, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 221, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 60, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 180, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 58, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 90, 221, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 120, 221, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 150, 221, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(70, 10, 58, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.isbnlookup)
        self.pushButton_2.clicked.connect(self.addbooks)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">ISBN</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Fill"))
        self.pushButton_2.setText(_translate("Dialog", "Add"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Title</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Author</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Location</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Book ID:"))
        self.label_6.setText(str(len(self.object.data_books)))


    def addbooks(self):
        isbn = self.lineEdit.text()
        title = self.lineEdit_2.text()
        author = self.lineEdit_4.text()
        if len(title) > 0:  
            self.object.addbook(title, author,isbn)
            self.lineEdit_2.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit.setText("")
            self.label_6.setText(str(len(self.object.data_books)))
            msg = QMessageBox()
            msg.setWindowTitle("Library")
            msg.setText("Book added")
            x = msg.exec_()
            self.window.populatebooks()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Library")
            msg.setText("ERROR: Please enter a title")
            x = msg.exec_()


    def isbnlookup(self):
        isbn = self.lineEdit.text()
        try:
            bookisbn = isbnlib.meta(str(isbn))
            # title = bookisbn['Title']
            if len(bookisbn) > 0:
                title = bookisbn['Title']
                authors = bookisbn['Authors']
                authors = " ".join(authors)
                
                self.lineEdit_2.setText(title)
                self.lineEdit_4.setText(authors)
                #self.object.addbook(title, authors,isbn)
                self.lineEdit_2.repaint()
                self.lineEdit_4.repaint()
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Library")
                msg.setText("ERROR: Invalid ISBN")
                x = msg.exec_()
        except isbnlib._exceptions.NotValidISBNError:
            msg = QMessageBox()
            msg.setWindowTitle("Library")
            msg.setText("ERROR: Invalid ISBN")
            x = msg.exec_()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())