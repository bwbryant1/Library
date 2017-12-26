import sys
import pkg_resources
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, qApp, QHBoxLayout, QMainWindow, QAction
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

        self.openAct = QAction(QIcon(self.getFileResource('folder.svg','icon')),'&Open Library', self)
        self.openAct.setShortcut('Ctrl+o')
        self.openAct.setStatusTip('Open Library')

        self.exitAct = QAction(QIcon(self.getFileResource('x.svg','icon')),'&Exit LibMan', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

    def createMenuBar(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        
        fileMenu = menu.addMenu('File')
        fileMenu.addAction('New..')
        fileMenu.addAction('Recent')
        fileMenu.addSeparator()
        fileMenu.addAction('Import..')
        fileMenu.addAction('Export..')
        fileMenu.addAction(self.openAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)
        
        editMenu = menu.addMenu('Edit')
        editMenu.addAction('Preferences')

        viewMenu = menu.addMenu('View')
        viewMenu.addAction('Go Fullscreen')
        
        aboutMenu = menu.addMenu('About')
        aboutMenu.addAction('About Library Manager...')

    def createToolBar(self):
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(self.openAct)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.exitAct)
    
    def setStatusBar(self,msg):
        self.statusBar().showMessage(str(msg))

def launch():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStatusBar("Welcome Back")
    window.showMaximized()
    window.show()
    app.exec_()
