import sqlite3
import os

def makeConnection(DATABASE_LOCATION):
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    return_this = []
    return_this.append(cur)
    return_this.append(con)
    return return_this

def makeNewLibrary(nameOf,locationOf):
	library_name = nameOf
	library_location = locationOf
	#method does use user inputted location yet	
	cwd = os.getcwd()
	
	try:
		connection = makeConnection(cwd + "/" + nameOf + ".db")
		cur = connection[0]
		con = connection[1]
	except sqlite3.Error as e:
		print(e)
	
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
	

	
