from datetime import datetime
import csv

# How wide is your table?
csvwidth = 12

# What is your source file?
infilename = "newaddressing.csv"

# What is your destination file?
outfilename = "new_addressing.html"

# Add 1 to csvwidth to include all columns.
csvwidth = csvwidth + 1

# Open the files I need.
with open(infilename, "r") as infile:
    with open(outfilename, "w") as outfile:

        # Write some HTML.
        outfile.write("<!DOCTYPE html>\n\n\
<html>\n\n\
<head>\n\
\t<meta charset=\"utf-8\">\n\
\t<meta name=\"description\" content=\"CSV with Python.\" />\n\
\t<meta name=\"author\" content=\"Jeremy's code.\" />\n\
\t<title>Addresses</title>\n\
\t<link rel=\"stylesheet\" href=\"css/addressstyle.css\" />\n\
\t<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js\"></script>\n\
\t<script src=\"js/addresshoverscript.js\"></script>\n\
</head>\n\n\
<body>\n\n\
\t<p>The following new addresses and address corrections have been recently assigned by the Frederick County Department of GIS.</p>\n\
\t<table>\n")

        # Loop for table.
        data = ""
        rownum = 0
        for row in csv.reader(infile):
            if rownum == 0: # Write th row.
                outfile.write("\t\t<tr>\n")
                colnum = 0
                for column in row:
                    colnum += 1
                    if colnum < csvwidth:
                        outfile.write("\t\t\t<th>" + column + "</th>\n")
                outfile.write("\t\t</tr>\n")
                rownum += 1
            else: # Write other rows.
                outfile.write("\t\t<tr>\n")
                colnum = 0
                for column in row:
                    colnum += 1
                    if colnum < csvwidth:
                        outfile.write("\t\t\t<td>" + column + "</td>\n")
                outfile.write("\t\t</tr>\n")
                rownum += 1

        # Finish HTML.
        outfile.write("\t</table>\n\
</html>")

        # Show success and number of records written.
        print("Finished. " + str(rownum) + " records written.")