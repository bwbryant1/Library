#!/usr/bin/env python
# coding: utf-8

import sys

from library import libraryItem as item

def main():
	libObj = item.libraryItem("45","Test Name","Test Desc")
	print(libObj)

# wow very main
if __name__ == "__main__":
    sys.exit(main())
