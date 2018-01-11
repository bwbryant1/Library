import sqlite3
import os

def makeConnection(DATABASE_LOCATION):
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    return_this = []
    return_this.append(cur)
    return_this.append(con)
    return return_this

def addBookToLibrary(libDir,nameOf):
    title = nameOf
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return_status['msg'] = "Could not make connection to that database"
        return return_status
    cur.execute("INSERT INTO BOOKS ('title') VALUES ('{title}')".format(title=title))
    con.commit()
    con.close()

def addInfoToBook(libDir,column,title,info):
    # E.g.) dbFuncs.addInfoToBook('/home/brandon/Documents/dev/Library/test.db','genre','Harry Potter','kids')
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return_status['msg'] = "Could not make connection to that database"
    return return_status

    bookExists = checkBookExists(libDir,title)['status']
    columnExists = checkColumnExists(libDir,column)['status']

    if bookExists and columnExists:
        try:
            cur.execute("UPDATE BOOKS SET {COLUMN} = '{INFO}' WHERE TITLE = '{TITLE}' ".format(COLUMN=column,INFO=info,TITLE=title))
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

def checkColumnExists(libDir,columnName):
    #E.g.) dbFuncs.checkColumnExists('/home/brandon/Documents/dev/Library/test.db','games')
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
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

def checkBookExists(libDir,title):
    #E.g.) dbFuncs.checkBookExists('/home/brandon/Documents/dev/Library/test.db','Harry Potter')
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
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
    return_status = {'status':True,'libDir':'','fileDir':'','msg':""}

    if locationOf == '':
        directory = os.getcwd()
    else:
        directory = locationOf
    return_status['libDir'] = directory
    return_status['fileDir'] = directory + "/" + nameOf + ".db"
    try:
        connection = makeConnection(directory + "/" + nameOf + ".db")
        cur = connection[0]
        con = connection[1]
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
        'isReading TEXT'
        ')')

    con.commit()
    con.close()
    return return_status
        
def searchLibrary(libDir, title):
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    bookExists = checkBookExists(libDir,title)['status']

    if bookExists:
        return_status['msg'] = "This is your book: " + title
        return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "This book cannot be found."
        return return_status

def listBooksInLibrary(libDir):
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE FROM BOOKS")
    bookListTuple = cur.fetchall()
    bookList = [x[0] for x in bookListTuple]
    return_status['bookList'] = bookList
    return return_status

def listReadingList(libDir):
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    cur.execute("SELECT TITLE FROM BOOKS WHERE isReading = 'True' ")
    bookListTuple = cur.fetchall()
    readingList = [x[0] for x in bookListTuple]
    return_status['readingList'] = readingList
    return return_status

def addBookToReadingList(libDir,title):
    return_status = {'status':True,'msg':""}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    bookExists = checkBookExists(libDir,title)['status']
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
