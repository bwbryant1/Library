import unittest
from library.libraryItem import libraryItem
  
class TestLibraryItem(unittest.TestCase):

	def setUp(self):
		self.libObj = libraryItem("4","Book","Book test")

	def test_object_create(self):
		self.libObj = ""
		self.libObj = libraryItem("4","Book","Book test")
		self.assertNotEqual(self.libObj , "")

	def test_getName(self):
		self.assertEqual(self.libObj.getName(),"Book")

	def test_setName(self):
		self.assertNotEqual(self.libObj.getName() , "NewName")
		self.libObj.setName("NewName")
		self.assertEqual(self.libObj.getName() , "NewName")

	def test_getID(self):
		self.assertEqual(self.libObj.getID(), "4")
	
	def test_setID(self):
		idToTest = "NewID"
		self.assertNotEqual(self.libObj.getID(),idToTest)
		self.libObj.setID(idToTest)
		self.assertEqual(self.libObj.getID(),idToTest)

	def test_getDescription(self):
		self.assertEqual(self.libObj.getDescription(),"Book test")

	def test_setDescription(self):
		descToTest = "Some Desc"
		self.assertNotEqual(self.libObj.getDescription(),descToTest)
		self.libObj.setDescription(descToTest)
		self.assertEqual(self.libObj.getDescription(),descToTest)

if __name__ == '__main__':
    unittest.main()
