"""
## Library Manager ##
## Author: Brandon Bryant ##
## Version: 1.0 ##
## Description: A skeleton class for library items ##
"""

class libraryItem(object):
	id = '404'
	
	def __repr(self):
		return '<id: %s>' % self.id
	
	def __init__(self,id,name,description):
		self.id = id
		self.name = name
		self.description = description

	def getName(self):
		return self.name

	def setName(self,newName):
		self.name = newName

	def getID(self):
		return self.id

	def setID(self,newID):
		self.id = newID

	def getDescription(self):
		return self.description

	def setDescription(self,newDescription):
		self.description = newDescription
