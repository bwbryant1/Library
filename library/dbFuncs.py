import sqlite3
import os

def makeConnection(DATABASE_LOCATION):
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    return (con,cur)

def addBookToLibrary(libPath,nameOfBook):
    return_status = {'status':True,'msg':""}

    if not checkBookExists(libPath,nameOfBook)['status']:
        try:
            con,cur = makeConnection(libPath)
        except sqlite3.Error as e:
            print(e)
            return_status['status'] = False
            return_status['msg'] = "Could not make connection to that database"
            return return_status
        cur.execute("INSERT INTO BOOKS ('TITLE') VALUES ('{TITLE}')".format(TITLE=nameOfBook))
        con.commit()
        con.close()
        return_status['msg'] = "Book Added"
        return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "Duplicate book name. Cant Add Book!"
        return return_status

def deleteBook(libPath,nameOfBook):
    return_status = {'status':True,'msg':""}

    if checkBookExists(libPath,nameOfBook)['status']:
            try:
                con,cur = makeConnection(libPath)
            except sqlite3.Error as e:
                print(e)
                return_status['status'] = False
                return_status['msg'] = "Could not make connection to that database"
                return return_status
            bookId = getBookId(libPath,nameOfBook)['bookId']
            cur.execute("DELETE FROM BOOKS WHERE ID = {ID}".format(ID=bookId))
            con.commit()
            con.close()
            return_status['msg'] = "Book Deleted!"
            return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "No book found to delete!"
        return return_status


def addInfoToBook(libPath,column,title,bookId,info):
    # E.g.) dbFuncs.addInfoToBook('/home/brandon/Documents/dev/Library/test.db','genre','Harry Potter','kids')
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return_status['msg'] = "Could not make connection to that database"
        return return_status
    columnExists = checkColumnExists(libPath,column)['status']

    if columnExists:
        try:
            cur.execute("UPDATE BOOKS SET {COLUMN} = '{INFO}' WHERE ID = {ID} ".format(COLUMN=column,INFO=info,ID=bookId))
        except:
            return_status['status'] = False
            return_status['msg'] = "Book %s not updated" % title
            return return_status
        return_status['msg'] = "Book %s updated succesfully" % title
    else:
        return_status['status'] = False
        return_status['msg'] = "Book or Column does not exist to perform UPDATE on"
        return return_status

    con.commit()
    con.close()
    return return_status

def checkColumnExists(libPath,columnName):
    #E.g.) dbFuncs.checkColumnExists('/home/brandon/Documents/dev/Library/test.db','games')
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return_status['msg'] = "Could not make connection to that database"
        return return_status

    try:
        cur.execute("SELECT {COLUMN} FROM BOOKS".format(COLUMN=columnName))
        return_status['status'] = "Column exists in the database"
        return return_status
    except:
        return_status['status'] = False
        return_status['msg'] = "Column does not exist in that database"
        return return_status

def checkBookExists(libPath,title):
    #E.g.) dbFuncs.checkBookExists('/home/brandon/Documents/dev/Library/test.db','Harry Potter')
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    try:
        cur.execute("SELECT TITLE FROM BOOKS WHERE TITLE = '{TITLE}' ".format(TITLE=title))
        if cur.fetchone()[0] == title:
            pass    
        else:
            raise Exception('No book found')
            return_status['msg'] = "Book exists in library"
        return return_status
    except:
        return_status['status'] = False
        return_status['msg'] = "Book does not exist in library"
        return return_status

def makeNewLibrary(nameOf,locationOf):
    library_name = nameOf
    library_location = locationOf
    return_status = {'status':True,'libDir':'','libPath':'','msg':""}

    if locationOf == '':
        directory = os.getcwd()
    else:
        directory = locationOf
    return_status['libDir'] = directory #This is the library Directory
    return_status['libPath'] = directory + "/" + nameOf + ".db" #This is the explicit library path
    try:
        con,cur = makeConnection(directory + "/" + nameOf + ".db")
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
        
    cur.execute('DROP TABLE IF EXISTS BOOKS')
    cur.execute(''
        'CREATE TABLE BOOKS ('
        'Id INTEGER PRIMARY KEY,'
        'title TEXT,'
        'author TEXT,'
        'ISBN TEXT,'
        'synopsis TEXT,'
        'picture BLOB,'
        'lastPageRead,'
        'genre TEXT,'
        'format TEXT,'
        'isReading TEXT,'
        'wantToRead TEXT,'
        'thumb BLOB,'
        'bookmark INTEGER'
        ')')

    con.commit()
    con.close()
    return return_status
        
def searchLibrary(libPath, title):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
      
    try:  
        cur.execute("SELECT TITLE FROM books WHERE title LIKE '%{NAME}%'".format(NAME = title))
        bookListTuple = cur.fetchall()
        bookList = [x[0] for x in bookListTuple]
        if bookList:
            return_status['bookList'] = bookList
            return_status['msg'] = "These are the books that match this title."
            return return_status
        else:
            return_status['status'] = False
            return_status['msg'] = "No books in library match that title."
            return return_status
    except:
        return_status['status'] = False
        return_status['msg'] = "No books in library match that title."
        return return_status

def listBooksInLibrary(libPath):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE,BOOKMARK FROM BOOKS")
    bookListTuple = cur.fetchall()
    bookList = [x for (x,y) in bookListTuple]
    bookmarkList = [y for (x,y) in bookListTuple]
    return_status['bookmarkList'] = bookmarkList
    return_status['bookList'] = bookList
    return_status['bookListTuple'] = bookListTuple
    return return_status

def listReadingList(libPath):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE FROM BOOKS WHERE isReading = 'True' ")
    bookListTuple = cur.fetchall()
    readingList = [x[0] for x in bookListTuple]
    return_status['readingList'] = readingList
    return return_status

def addBookToReadingList(libPath,title):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    bookExists = checkBookExists(libPath,title)['status']
    if bookExists:
        try:
            cur.execute("UPDATE BOOKS SET isReading = 'True' WHERE TITLE = '{TITLE}' ".format(TITLE=title))
            con.commit()
            con.close()
        except:
            return_status['status'] = False
            return_status['msg'] = "Failed to add book to reading list. Could not update reading list."
            return return_status
        return_status['msg'] = "Added book to reading list"
        return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "Failed to add book to reading list. Book !Exist?"
        return return_status

def sortLibrary(libPath,sortBy):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE, AUTHOR FROM BOOKS ORDER BY UPPER({COLUMN})".format(COLUMN=sortBy))
    sortedListTuple = cur.fetchall()
    sortedList = [x for (x,y) in sortedListTuple]
    columnList = [y for (x,y) in sortedListTuple]
    return_status['sortedList'] = sortedList
    return_status['columnList'] = columnList
    return_status['sortedListTuple'] = sortedListTuple
    return_status['sortedList'] = sortedList
    return return_status

def getBookId(libPath,title):
    #E.g.) dbFuncs.checkBookExists('/home/brandon/Documents/dev/Library/test.db','Harry Potter')
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
    try:
        cur.execute("SELECT ID FROM BOOKS WHERE TITLE = '{TITLE}' ".format(TITLE=title))
        bookIdTuple = cur.fetchone()
        bookId = bookIdTuple[0]
        return_status['bookId']= bookId
        return_status['msg'] = 'Book Found!'
        return return_status
    except:
        return_status['msg'] = 'Sorry Book not found'
        return return_status

def addToRead(libPath, title):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
    
    bookExists = checkBookExists(libPath,title)['status']
    if bookExists:
        try:
            cur.execute("UPDATE BOOKS SET wantToRead = 'True' WHERE TITLE = '{TITLE}' ".format(TITLE=title))
            con.commit()
            con.close()
        except:
            return_status['status'] = False
            return_status['msg'] = "Failed to add book to Want to Read list. Could not update list."
            return return_status
        return_status['msg'] = "Added book to Want To Read list"
        return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "Failed to add book to Want To Read list. Book !Exist?"
        return return_status

def listToRead(libPath):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE FROM BOOKS WHERE wantToRead = 'True' ")
    bookListTuple = cur.fetchall()
    toReadList = [x[0] for x in bookListTuple]
    return_status['wantToReadList'] = toReadList
    return return_status

def getBookmark(libPath,pageNumber):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

