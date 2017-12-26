import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, qApp, QHBoxLayout, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle('Library Manager 0.1')
        self.setMinimumSize(800,400)
        self.createActions()
        self.createMenuBar()
        self.createToolBar()

    def createActions(self):
        self.exitAct = QAction(QIcon('exit.png'),'&Exit LibMan', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

    def createMenuBar(self):
        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        
        fileMenu = menu.addMenu('File')
        fileMenu.addAction(self.exitAct)
        
        editMenu = menu.addMenu('Edit')
        editMenu.addAction('Preferences')

        viewMenu = menu.addMenu('View')
        viewMenu.addAction('Go Fullscreen')
        
        aboutMenu = menu.addMenu('About')
        aboutMenu.addAction('About Library Manager...')

    def createToolBar(self):
        self.toolbar = self.addToolBar('Exit')
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
