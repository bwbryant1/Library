'''
## Library Manager ##
## Author: Brandon Bryant ##
## Version: 1.0 ##
## Description: A skeleton class for library items ##
'''

'''
LibraryItemsSupported = ['Books','Movies','Contacts','Games']
'''

class libraryItem(object):
    id = '404'
	
    def __repr__(self):
	return '<uid: %s>' % self.uid
	
    def __init__(self,uid,name):
	self.uid = uid #The UID will be a randomly generated value
	self.name = name #The simple name of the generic item
	self.description = '' #A Description of the item

    def getName(self):
	return self.name

    def setName(self,newName):
	self.name = newName

    def getUID(self):
	return self.uid

    def setUID(self,newUID):
	self.uid = newUID

    def getDescription(self):
        if self.description:
	    return self.description
        else:
            return 'No set description'

    def setDescription(self,newDescription):
	self.description = newDescription

class bookItem(object):
    def __repr__(self):
        return '<uid: %s>' % self.uid 

    def __init__(self,uid,name):
        self.uid = uid #The UID will be a randomly generated value
        self.name = name #The name of the book
        self.description = '' #A description of the book, maybe the synopsis
        self.isbn = ''
    
