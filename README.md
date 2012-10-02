CSV to HTML Table
=================

Latest Changes
--------------

* 0.3.6: Replaced text entries with file dialogs.

Purpose
-------

This was born from necessity.  At work, we have lots of data in CSV format that people want to display on the web.  Sometimes, it's convenient to have that CSV feed some sort of DBMS that can be queried by a web application; other times, we just need a quick HTML table.  This answers the second need by reading through the CSV and spitting out an HTML table that can then be plugged into a web page, like in the example.

Usage
-----

Use the buttons to browse to and choose source and destination files.  The "Columns to include" box is specifically for CSVs we get at work that for some reason have extra empty columns.  If this feature is not needed, it can simply be left blank.  Click the "Create" button and the HTML will be written.  You can then copy the HTML and paste it where it needs to go.  My first version of this script is in the "addresswriter.py" script.  That version creates an entire HTML page, but I wanted the GUI version here to be useful for any table needing to go into a page; therefore, this just writes out the table.

Included is the setup file I used to create EXE and MSI with [cx_Freeze](http://cx-freeze.sourceforge.net/) that I can deploy to users at work.

Requirements
------------

I tested this with Python 3.2.  As far as I know, it'll work with Python 2.7 if you change `from tkinter import *` to `from Tkinter import *` (difference: capitalization) and `import tkinter.messagebox as box` to `import tkMessageBox as box`.  You also need the Tkinter library, but I think that comes with Python (at least, it did on Windows).  Other than that, all you need is a CSV file.

Future
------

This is definitely not a lesson in good UI design nor is it an example of great programming.  I think I need to handle errors better.  The code is kind of messy -- just one long script.  I'd like to clean it up soon.