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
    return_status = {'status':True}

    try:
        connection = makeConnection(libDir)
        cur = connection[0]
        con = connection[1]
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
    cur.execute("INSERT INTO BOOKS ('title') VALUES ('{title}')".format(title=title))
    con.commit()
    con.close()

def makeNewLibrary(nameOf,locationOf):
    library_name = nameOf
    library_location = locationOf
    return_status = {'status':True,'libDir':'','fileDir':''}

    #method does use user inputted location yet	
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
        'format TEXT'
        ')')

    con.commit()
    con.close()
    return return_status

	
