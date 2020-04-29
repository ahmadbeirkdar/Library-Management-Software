
# Library  Software  In Python

This Project is now on hold, I have made a mistake and wrote this in python. I should not have. 

Follow this link for the new project in C++ being worked on https://github.com/ahmadbeirkdar/Library-Management-Software

Current Features:

* Storing books, users and the sign in and sign out of the books

* User and book search

* Due dates, and extensions

* Adding books to database, with ISBN autofill


What is planned soon/TODO:

* Cleaning up code(OOP, and cleaning up my messy quick code)

* Dues and an email system

* A settings panel

* Managment of multiple libraries 

CSV columns for each file, the following format will stay:

* books.csv - Col 1 ID(From 0 to whatever), Col 2 Title, Col 3 Author, Col 4 ISBN, Col 5 Location

* users.csv - Col 1 ID(From 0 to whatever), Col 2 name, Col 3 username, Col 4 email, Col 5 Dues

Small Video Showcase:

* Note: This is as of March 30,2020, this may not be full up to date.

[![](http://img.youtube.com/vi/8VYFRdHUryc/0.jpg)](http://www.youtube.com/watch?v=8VYFRdHUryc "")

How to Use:

* Have the following CSVs from what is listed above, after the 5th columns, you can put whatever data you want the program wont touch it
* Have the following CSVs in the folder of the guisetup.py folder. 
* Simply run with python3 as follows --> python3 guisetup.py

Files:

* test.py, is a simple test file to show real world use, but this is the non-GUI implementation

* datafunc.py, ok I agree an ugly name, but this is the feel in which all the functions are stored for now

* classes.py, pretty clear, where the classes for the parser, books and users is stored, I don't see this file changing drastically for now. Maybe some small additions or changes

* guisetup.py, this file is just to setup all the classes and functions for the gui, it will most likely expand

* gui folder, includes everything gui

http://ahmad.ltd
