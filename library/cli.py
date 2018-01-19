#!/usr/bin/env python
# coding: utf-8

'''
Variable List:
    libPath : explicit file path to library
    libDir : the directory where the library resides
    choice : the value gathered from the user input
    <func>['status'] : usually a True or False value
    dbFuncs : a module with an assortment of functions to manipulate sqlite3 database
    nameOfBook : The name of the book title
'''

import sys,os
from . import dbFuncs

DEBUG = False

def clearTerm(): #This will not work on window. Need to add check for windows, then implement fix
    os.system("clear")

def new_library():
    clearTerm()
    if DEBUG:
        print("new_library\n")
    dbName = input('What do you want to call your Library?: ') #This will be the name of the file/database
    while(not dbName): #This while loops ensures that the filename is !blank
        dbName = input("Library name cannot be blank. What do you want to call your Library?: " )
    libDir = input('Where do you want to store your Library?: ')  #this is the directory where the library will be kept. USB/HDD/Net
    libFunc = dbFuncs.makeNewLibrary(dbName,libDir) #This will just give us a return status of the make library function
    if libFunc['status']: #This is our returned dictionary that gives us our statuses, usually a True or False value, and various other things.
        print("made library at: %s" % libFunc['libPath'] )
    else:
        print("Could not make new library at: %s" % libFunc['libPath'])

def load_library():
    clearTerm()
    running = True
    if DEBUG:
        print("load_library\n")
    libPath = input("Where is the library?: ") 
    print("Checking file at %s" % libPath)
    if os.path.isfile(libPath):
        print("Library Exists. Loading library.")
        while running:
            print(
                "Using library {LIBPATH}. \n" 
                " 1) List Books \n"
                " 2) Add Book \n"
                " 3) Delete Book \n"
                " 4) Add book to Reading list \n"
                " 5) View Reading list \n"
                " 6) Update book \n"
                " 7) Find Book \n"
                " 8) Sort Library \n"
                " 9) Add book to Want To Read list \n"
                "10) List Want To Read list \n"
                "11) Update bookmark \n"
                "99) Close library \n"
                "".format(LIBPATH=libPath)) 
            choice = input("What do you want to do?: ")
            if choice == '99':
                clearTerm()
                running = False
            elif choice == '1':
                clearTerm()
                print("========BOOKS========")
                bookListTuple = dbFuncs.listBooksInLibrary(libPath)['bookListTuple']
                for _book,_bookmark in bookListTuple:
                    print("Title: "+ _book + " | Bookmark: "+ str(_bookmark))
                print("========END OF BOOKS========")
            elif choice == '2':
                clearTerm()
                print("Adding book")
                nameOfBook = input("What is the name of the book?: ")
                while(not nameOfBook):
                    nameOfBook = input("Name of book cannot be blank! Try again: ")
                print(dbFuncs.addBookToLibrary(libPath,nameOfBook)['msg'])
                
            elif choice == '4':
                clearTerm()
                nameOfBook = input("What is the name of the book you would like to add to your reading list?: ")
                while(not nameOfBook):
                    nameOfBook = input("Book name cannot be blank. Try again: ")
                print(dbFuncs.addBookToReadingList(libPath,nameOfBook)['msg'])
            elif choice == '5':
                clearTerm()
                print("=====Reading List=====")
                readingList = dbFuncs.listReadingList(libPath)['readingList']
                for _book in readingList:
                    print(_book)
                print("=====End of List=====")
            elif choice == '6':
                clearTerm()
                nameOfBook = input("What is the title of the book you would like to update?:")
                if(dbFuncs.checkBookExists(libPath,nameOfBook)['status']):
                    bookId = dbFuncs.getBookId(libPath, nameOfBook)['bookId']
                    print(
                        " 1) Update Author \n"
                        " 2) Update Genre \n"
                        " 3) Update Format \n")
                    columnNum = input("Which feature would you like to update?")
                    if columnNum == '1':
                        column = 'author'
                    elif columnNum == '2':
                        column = 'genre'
                    elif columnNum == '3':
                        column = 'genre'
                    info = input("Please provide the info for the %s column:" % column)
                    print(dbFuncs.addInfoToBook(libPath,column,nameOfBook,bookId,info)['msg'])
                else:
                    print("Sorry Book %s not found" % nameOfBook)
            elif choice == '7':
                clearTerm()
                print("Find a book")
                nameOfBook = input("What is the name of the book you would like to find?: ")
                results = dbFuncs.searchLibrary(libPath, nameOfBook)
                if(results['status']):
                    print(results['msg'])
                    matches = results['bookList']
                    for _book in matches:
                        print(_book)
                else:
                    print(results['msg'])
            elif choice == '8':
                clearTerm()
                print(
                    "1) Sort by Title \n"
                    "2) Sort by Author")
                sortByNum = input("What would you like to sort by: ")
                if sortByNum == '1':
                    sortBy = 'title'
                elif sortByNum == '2':
                    sortBy= 'author'
                else:
                    print("Sorry that's not a defined choice")
                print("===== Sorted List=====")
                sortedListTuple = dbFuncs.sortLibrary(libPath,sortBy)['sortedListTuple']
                for _book,_author in sortedListTuple:
                    print("Title: "+ _book + "\n"+ "    By: "+ str(_author))
                print("=====End of Sorted List=====")
            elif choice == '9':
                clearTerm()
                nameOfBook = input("What is the name of the book you would like to add to your Want To Read list?: ")
                while(not nameOfBook):
                    nameOfBook = input("Book name cannot be blank. Try again: ")
                print(dbFuncs.addToRead(libPath,nameOfBook)['msg'])
            elif choice == '10':
                clearTerm()
                print("=====Want To Read List=====")
                toReadList = dbFuncs.listToRead(libPath)['wantToReadList']
                for _book in toReadList:
                    print(_book)
                print("=====End of List=====")
            elif choice == '11':
                clearTerm()
                nameOfBook = input("What is the name of the book you would like to update bookmark for?: ")
                while(not nameOfBook):
                    nameOfBook = input("You must input a book name. Try Again: ")
                if(dbFuncs.checkBookExists(libPath,nameOfBook)['status']):
                    print("What do you want to do?")
                    choice = input(""
                            "1) Set bookmark \n"
                            "2) Delete bookmark \n"
                            "Choice: ")
                    if choice == '1':
                        pageNumber = input("What page is the bookmark?: ")
                        if(pageNumber.isdigit()):
                            bookId = dbFuncs.getBookId(libPath, nameOfBook)['bookId']
                            return_status = dbFuncs.addInfoToBook(libPath,'bookmark',nameOfBook,bookId,int(pageNumber))['msg']
                        else:
                            print("input was not a number!")
                    elif choice == '2':
                        bookId = dbFuncs.getBookId(libPath, nameOfBook)['bookId']
                        return_status = dbFuncs.addInfoToBook(libPath,'bookmark',nameOfBook,bookId,0)['msg']
                    else:
                        print("Input not valid.")
                else:
                    print("I did not find book: {book}".format(book=nameOfBook))

            else:
                print("Selection not recognized")
    else:
        print("We did not find a library there. Sorry")

def get_library_details():
    if DEBUG:
        print("get_library_details\n")
def search_for_databases():
    if DEBUG:
        print("search_for_databases\n")

def main():
    os.system("clear")
    print("Libraryman running. Welcome.\n")
    while True:
        print(
            "Supported Functions are: \n"
            " 1) Make a new Library \n"
            " 2) Load a Library from file \n"
            " 3) Get Library details \n"
            " 4) Search for Databases \n"
            "99) Exit \n")

        choice = input("What would you like to do?: ")
        if choice == '1':
            print("Making Library")
            new_library()
        elif choice == '2':
            print("Loading Library")
            load_library()
        elif choice == '3':
            print("Getting library Details")
            get_library_details()
        elif choice == '4':
            print("Searching for Databases")
            search_for_databases()
        elif choice == '99':
            clearTerm()
            print("Exiting now.")
            sys.exit(0)
        else:
            print("I'm sorry I don't know that command.\n")

# wow very main
if __name__ == "__main__":
    sys.exit(main())

