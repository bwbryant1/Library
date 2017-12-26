#!/usr/bin/env python
# coding: utf-8

import sys
from library import libraryItem as item
from . import gui

def main():
    libObj = item.libraryItem("45","Test Name","Test Desc")
    print(libObj)
    gui.launch()
    print("All done, closing..")

# wow very main
if __name__ == "__main__":
    sys.exit(main())
