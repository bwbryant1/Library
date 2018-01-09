#!/usr/bin/env python
# coding: utf-8

import sys,os
from library import libraryItem as item

DEBUG = True

currLibrary = ''

def new_library():
	if DEBUG:
		print("new_library\n")
def load_library():
	if DEBUG:
		print("load_library\n")
def get_library_details():
	if DEBUG:
		print("get_library_details\n")
def search_for_databases():
	if DEBUG:
		print("search_for_databases\n")


def main():
	running = True
	os.system("clear")
	print("Libraryman running. Welcome.\n")
	while running:
		print("Supported Functions are:\n 1) Make a new Library\n 2) Load a Library from memory\n 3) Get Library details\n 4) Search for Databases")
		print("10) Exit")
		choice = input("What would you like to do?: ")
		if choice == '1':
			print("Making Library")
			new_library()
		elif choice == '2':
			print("Loading Library")
			load_library()
		elif choice == '3':
			print("Getting library Details")
			get_library_details()
		elif choice == '4':
			print("Searching for Databases")
			search_for_databases()
		elif choice == '10':
			print("Exitting now.")
			sys.exit(0)
		else:
			print("I'm sorry I don't know that command.\n")

		
# wow very main
if __name__ == "__main__":
	sys.exit(main())

