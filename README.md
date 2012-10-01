CSV to HTML Table
=================

Purpose
-------

This was born from necessity.  At work, we have lots of data in CSV format that people want to display on the web.  Sometimes, it's convenient to have that CSV feed some sort of DBMS that can be queried by a web application; other times, we just need a quick HTML table.  This answers the second need by reading through the CSV and spitting out an HTML table that can then be plugged into a web page, like in the example.

Usage
-----

Type your source and destination file locations in the text boxes.  The "Columns to include" box is specifically for CSVs we get at work that for some reason have extra empty columns.  If this feature is not needed, it can simply be left blank.  Click the "Create" button and the HTML will be written.  You can then copy the HTML and paste it where it needs to go.  My first version of this script is in the "addresswriter.py" script.  That version creates an entire HTML page, but I wanted the GUI version here to be useful for any table needing to go into a page; therefore, this just writes out the table.

Included is the setup file I used to create EXE and MSI with [cx_Freeze](http://cx-freeze.sourceforge.net/) that I can deploy to users at work.

Requirements
------------

I tested this with Python 3.2.  As far as I know, it'll work with Python 2.7 if you change `from tkinter import *` to `from Tkinter import *` (difference: capitalization).  Other than that, all you need is a CSV file.

Future
------

This version is way early.  I definitely need to handle exceptions better.  I also intend to add a dialog box for finding the source file instead of requiring the user to type the path.