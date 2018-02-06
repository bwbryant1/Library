import unittest
import os
import library.dbFuncs as dbFuncs
import library.insert_image as inImage

class TestDbFuncsItem(unittest.TestCase):
    
    def setUp(self):
        self.testLibraryName = "test"
        self.testLibDir = "./test.db"
        self.fakeBook = "This is not a book!"
        self.realBook = "How to fail a class"
        self.realBookTwo = "Is this all worth it"
        self.realBookThree = "DCCSAD"
        self.pageNumberForBookThree = "45"
        self.imageName = "test.jpg"
        dbFuncs.makeNewLibrary(self.testLibraryName,".")

    def test_makeLibrary(self):
        self.assertEqual(os.path.isfile(self.testLibDir) , True)

    def test_uploadCoverPhoto(self):
        status = inImage.storeImageInLibrary(self.testLibDir,self.imageName)['status']
        self.assertEqual(status , True)

    def test_addBookToLibrary(self):
        status = dbFuncs.addBookToLibrary(self.testLibDir,self.realBook)['status']
        self.assertEqual(status,True)

    def test_checkBookExists(self):
        dbFuncs.addBookToLibrary(self.testLibDir,self.realBook)['status']
        self.assertEqual(dbFuncs.listBooksInLibrary(self.testLibDir)['bookList'][0],self.realBook)

    def test_checkBookmark(self):
        dbFuncs.addBookToLibrary(self.testLibDir,self.realBook)['status']
        status = dbFuncs.addInfoToBook(self.testLibDir,'bookmark',self.realBook,1,self.pageNumberForBookThree)['status']
        self.assertEqual(status , True)

    def test_sortByAuthor(self):
        status = dbFuncs.sortLibrary(self.testLibDir,"author")['status']
        self.assertEqual(status , True)

    def test_addBookToReadingList(self):
        status = dbFuncs.addToRead(self.testLibDir,self.realBook)['status']
        self.assertEqual(status , False)

    def test_viewListInWantToRead(self):
        status = dbFuncs.listToRead(self.testLibDir)['status']
        self.assertEqual(status , True)

    def test_sortByTitle(self):
        status = dbFuncs.sortLibrary(self.testLibDir,"title")['status']
        self.assertEqual(status , True)

    def test_checkBookExistsError(self):
        self.assertEqual(dbFuncs.checkBookExists(self.testLibDir,self.fakeBook)['status'],False)

    def test_updateAuthor(self):
        dbFuncs.addBookToLibrary(self.testLibDir,self.realBook)['status']
        status = dbFuncs.addInfoToBook(self.testLibDir,'author',self.realBook,1,"newAuthor")['status']
        self.assertEqual(status , True)

    def test_deleteBook(self):
        self.assertNotEqual(dbFuncs.deleteBook(self.testLibDir,self.realBook)['status'],True)
        pass

    def test_checkLibraryNotExist(self):    
        self.assertNotEqual(os.path.isfile("./testFake.db") , True)


if __name__ == '__main__':
    unittest.main()
