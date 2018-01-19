import sys
import pkg_resources
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, qApp, QHBoxLayout, QMainWindow, QAction, QMessageBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.resource_package = __name__
        self.iconsFolder = 'icons'
        self.setWindowTitle('Library Manager 0.1')
        self.setMinimumSize(800,400)
        self.createActions()
        self.createMenuBar()
        self.createToolBar()

    def getFileResource(self,name,type):
        if type == 'icon':
            self.resourceFolder = self.iconsFolder
        
        resource_path = '/'.join((self.resourceFolder, name))
        return pkg_resources.resource_filename(self.resource_package, resource_path)

    def createActions(self):
        
        self.saveAct = QAction(QIcon(self.getFileResource('sync.svg','icon')),'&Open Library', self)
        self.saveAct.setShortcut('Ctrl+s')
        self.saveAct.setStatusTip('Save Library')

        self.openAct = QAction(QIcon(self.getFileResource('gear.svg','icon')),'&Open Library', self)
        self.openAct.setShortcut('Ctrl+o')
        self.openAct.setStatusTip('Open Library')

        self.exitAct = QAction(QIcon(self.getFileResource('x.svg','icon')),'&Exit LibMan', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

        self.aboutAct = QAction("&About", self,
        statusTip="Show the application's About box",
        triggered=self.about)

    def createMenuBar(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        
        fileMenu = menu.addMenu('File')
        fileMenu.addAction('New Library')
        fileMenu.addAction('Recent')
        fileMenu.addSeparator()
        fileMenu.addAction('Import items')
        fileMenu.addAction('Export items')
        fileMenu.addAction(self.openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)
        
        editMenu = menu.addMenu('Edit')
        editMenu.addAction('Undo')
        editMenu.addAction('Redo')
        editMenu.addAction('Add Selected to Reading List')
        editMenu.addAction('Delete Selected')
        editMenu.addAction('Preferences')

        viewMenu = menu.addMenu('View')
        viewMenu.addAction('Hide Sidebar')
        viewMenu.addAction('Increase List Size')
        viewMenu.addAction('Decrease List Size')
        viewMenu.addAction('Go Fullscreen')
        
        aboutMenu = menu.addMenu('About')
        aboutMenu.addAction(self.aboutAct)

    def createToolBar(self):
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.openAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.exitAct)
    
    def setStatusBar(self,msg):
        self.statusBar().showMessage(str(msg))

    def about(self):
        QMessageBox.about(self, "About Library Manager",
                "The <b>Library Manger</b> app was made for CYEN 481"
                "<br>Its Authors are: Brandon Bryant, Caroline Fontenot, and Sai Spurthy")

def launch():
    app = None
    if ( not QApplication.instance() ):
        # create a new application
        app = QApplication(sys.argv)

    window = MainWindow()
    window.setStatusBar("Welcome Back")
    window.showMaximized()
    window.show()
    app.exec_()
