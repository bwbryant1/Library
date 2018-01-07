# Library Manager

<h2>Overview</h2>
<p>
Our library application will manage a collection books, both physical and digital. Core functionality of the application will allow Users will be able to Add, Remove, and Search books in their library. 
</p>
<br>
Install Instructions:

1) git clone https://www.github.com/bwbryant1/Library.git
2) pip3 install virtualenv
3) virtualenv -p python libraryDev #this makes a virtual environment to test out software, without installing all the dependencies on your computer
4) cp -R Library/ libraryDev/ #Make a development copy of the module
5) cd libraryDev/
6) source bin/active #This activates the virtual environment. It has its own python3 local installation that you can destroy and mess things up with
7) python3 setup.py install
8) libraryman 

Develop Install Instructions:
  1) *Same as 1-6 before*
  2) python3 setup.py develop
  3) libraryman *And then close application when done*
  4) *make some feature change*
  5) libraryman *application will now run, reflecting the changes you made to source code*
  6) *when satified with the change, overwrite the changed file to the ./Library/ dir outside of ./libraryDev *


When done with development:
  1) deactivate
  2) cd ../Library/
  3) git add *
  4) git commit -m "made some feature change, etc.."
  5) git push
