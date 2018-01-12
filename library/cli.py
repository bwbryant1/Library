#!/usr/bin/env python
# coding: utf-8

import sys,os
from . import dbFuncs

DEBUG = True

def clearTerm():
    os.system("clear")

def new_library():
    clearTerm()
    if DEBUG:
        print("new_library\n")
    dbName = input('What do you want to call your Library?: ')
    while(not dbName):
        dbName = input("Library name cannot be blank. What do you want to call your Library?: " )
    location = input('Where do you want to store your Library?: ')	
    libFunc = dbFuncs.makeNewLibrary(dbName,location)
    if libFunc['status']:
        print("made library at: %s" % libFunc['fileDir'] )
        pass
    else:
        print("Could not make new library at: %s" % libFunc['fileDir'])

def load_library():
    clearTerm()
    running = True
    if DEBUG:
        print("load_library\n")
    fileDir = input("Where is the library?: ")
    print("Checking file at %s" % fileDir)
    if os.path.isfile(fileDir):
        print("Library Exists. Loading library.")
        while running:
            print(
                "Using library {lib}. \n" 
                " 1) List Books \n"
                " 2) Add Book \n"
                " 3) Delete Book \n"
                " 4) Add book to Reading list \n"
                " 5) View Reading list \n"
                " 6) Update book \n"
                " 7) Find Book \n"
                " 8) Sort Library \n"
                "10) Close library"
                "".format(lib=fileDir)) 
            choice = input("What do you want to do?: ")
            if choice == '10':
                clearTerm()
                running = False
            elif choice == '1':
                clearTerm()
                print("========BOOKS========")
                bookList = dbFuncs.listBooksInLibrary(fileDir)['bookList']
                for _book in bookList:
                    print(_book)
                print("========END OF BOOKS========")
            elif choice == '2':
                print("Adding book")
                nameOfBook = input("What is the name of the book?: ")
                while(not nameOfBook):
                    nameOfBook = input("Name of book cannot be blank! Try again: ")
                dbFuncs.addBookToLibrary(fileDir,nameOfBook)
            elif choice == '4':
                nameOfBook = input("What is the name of the book you would like to add to your reading list?: ")
                while(not nameOfBook):
                    nameOfBook = input("Book name cannot be blank. Try again: ")
                print(dbFuncs.addBookToReadingList(fileDir,nameOfBook)['msg'])
            elif choice == '5':
                clearTerm()
                print("=====Reading List=====")
                readingList = dbFuncs.listReadingList(fileDir)['readingList']
                for _book in readingList:
                    print(_book)
                print("=====End of List=====")
            elif choice == '7':
                print("Find a book")
                nameOfBook = input("What is the name of the book you would like to find?: ")
                results = dbFuncs.searchLibrary(fileDir, nameOfBook)
                if(results['status']):
                	print(results['msg'])
                	matches = results['bookList']
                	for _book in matches:
                		print(_book)
                else:
                	print(results['msg'])
            elif choice == '8':
                clearTerm()
                sortBy = 'title'
                sortedList = dbFuncs.sortLibrary(fileDir,sortBy)['sortedList']
                for _book in sortedList:
                    print(_book)
                print("=====End of Sorted List=====")
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
            "10) Exit \n")

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
        elif choice == '10':
            clearTerm()
            print("Exiting now.")
            sys.exit(0)
        else:
            print("I'm sorry I don't know that command.\n")

# wow very main
if __name__ == "__main__":
    sys.exit(main())

