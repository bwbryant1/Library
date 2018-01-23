import io
import sqlite3
from PIL import Image

def makeConnection(DATABASE_LOCATION):
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    return (con,cur)

def getImageBytes(path):
    return_status = {'status':False,'msg':""}
    try:
        im = Image.open(path)
        byteField = io.BytesIO()
        im.save(byteField, 'GIF')
        return_status['byteField'] = byteField.getvalue()
        return_status['status'] = True
        return return_status
    except:
        return_status['status'] = False
        return return_status

def storeImageInLibrary(libPath,imgPath):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status

    imgBytesDict = getImageBytes(imgPath)
    if imgBytesDict['status']:
        byteField = imgBytesDict['byteField']
        cur.execute("insert into BOOKS (thumb) values (?)", (memoryview(byteField),))
        con.commit()
        con.close()
        return_status['msg'] = "Stored image in library"
        return return_status
    else:
        return_status['status'] = False
        return_status['msg'] = "Could not store image in library"
        return return_status

def getThumbnailBytes(libPath,bookId):
    return_status = {'status':True,'msg':""}

    try:
        con,cur = makeConnection(libPath)
    except sqlite3.Error as e:
        print(e)
        return_status['status'] = False
        return return_status
    try:
        cur.execute("select thumb from books where id = {ID}".format(ID=bookId))
        imageTuple = cur.fetchall()
        return_status['imageBytes'] = imageTuple[0][0]
        return return_status
    except:
        return_status['msg'] = "Could not fetch thumbnail bytes"
        return_status['status'] = False
        return return_status


