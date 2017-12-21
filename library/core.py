#!/usr/bin/env python
# coding: utf-8

import sys
from library import libraryItem as item
from PyQt5 import QtWidgets

def main():
    libObj = item.libraryItem("45","Test Name","Test Desc")
    print(libObj)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    button = QtWidgets.QPushButton("Begin PyQt5 window test")
    window.setCentralWidget(button)
    window.show()
    app.exec_()

# wow very main
if __name__ == "__main__":
    sys.exit(main())
