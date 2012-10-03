from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as box
import csv
import os


infilename = ""
outfilename = ""

class Application(Frame):

	def make_table(self):

		includeColumns = ""

		# Handle whether txtColumns is filled.
		if len(self.txtColumns.get()) == 0:
			includeColumns = "0"
			includeColumns = int(includeColumns)
		else:
			try:
				includeColumns = int(self.txtColumns.get())
			except ValueError:
				# Show type error.
				self.lblResult["text"] = "Error. Make sure your columns value is either blank or an integer."
				self.lblResult["fg"] = "#ef102a"
				raise
				# Do this better.

		try:
			with open(self.infilename, "r") as infile:
				with open(self.outfilename, "w") as outfile:
		
					# Write some HTML.
					outfile.write("<!-- START COPYING HTML HERE. -->\n")
					outfile.write("<table")
					if len(self.txtClass.get()) > 0:
						outfile.write(" class=\"" + self.txtClass.get() + "\"")
					if len(self.txtId.get()) > 0:
						outfile.write(" id=\"" + self.txtId.get() + "\"")
					outfile.write(">\n")

					# Loop for table.
					rownum = 0
					for row in csv.reader(infile):
						if rownum == 0: # Write th row.
							outfile.write("\t<thead>\n")
							outfile.write("\t\t<tr>\n")
							colnum = 0
							for column in row:
								colnum += 1
								if includeColumns > 0:
									if (colnum - 1) < includeColumns:
										outfile.write("\t\t\t<th>" + column + "</th>\n")
								else:
									outfile.write("\t\t\t<th>" + column + "</th>\n")
							outfile.write("\t\t</tr>\n")
							outfile.write("\t</thead>\n")
							outfile.write("\t<tbody>\n")
							rownum += 1
						else: # Write other rows.
							outfile.write("\t\t<tr>\n")
							colnum = 0
							for column in row:
								colnum += 1
								if includeColumns > 0:
									if (colnum - 1) < includeColumns:
										outfile.write("\t\t\t<td>" + column + "</td>\n")
								else:
									outfile.write("\t\t\t<td>" + column + "</td>\n")
							outfile.write("\t\t</tr>\n")
							rownum += 1

					# Finish table.
					outfile.write("\t</tbody>\n")
					outfile.write("</table>\n")
					outfile.write("<!-- STOP COPYING HTML HERE. -->")

					# Show records written.
					self.lblResult["text"] = "Finsihed. " + str(rownum) + " records written."
					self.lblResult["fg"] = "#007f3f"
		except:
			# Show error.
			self.lblResult["text"] = "Error.  Make sure your source and destination paths are valid."
			# self.lblResult["text"] = sys.exc_info()
			self.lblResult["fg"] = "#ef102a"
			# Do this better.

	def createWidgets(self):

		bigFrame = Frame(root, bd=1, relief=RAISED)

		fileFrame = Frame(bigFrame)
		# Infile
		self.btnGetInFile = Button(fileFrame, text="Source", command=self.getInFile, width="10")
		self.btnGetInFile.pack()
		self.lblInFilePicked = Label(fileFrame, fg="#1624bc")
		self.lblInFilePicked.pack()
		# Outfile
		self.btnGetOutFile = Button(fileFrame, text="Destination", command=self.getOutFile, width="10")
		self.btnGetOutFile.pack()
		self.lblOutFilePicked = Label(fileFrame, fg="#1624bc")
		self.lblOutFilePicked.pack()
		fileFrame.pack()

		columnFrame = Frame(bigFrame)
		# Columns
		self.lblColumns = Label(columnFrame, text="Include columns (leave blank for all):")
		self.lblColumns.pack({"side": "left"})
		self.txtColumns = Entry(columnFrame, width="10")
		self.txtColumns.pack({"side": "right"})
		columnFrame.pack()

		classFrame = Frame(bigFrame)
		# Class
		self.lblClass = Label(classFrame, text="Table class (leave blank for none):")
		self.lblClass.pack({"side": "left"})
		self.txtClass = Entry(classFrame, width="10")
		self.txtClass.pack({"side": "right"})
		classFrame.pack()

		idFrame = Frame(bigFrame)
		# ID
		self.lblId = Label(idFrame, text="Table ID (leave blank for none):")
		self.lblId.pack({"side": "left"})
		self.txtId = Entry(idFrame, width="10")
		self.txtId.pack({"side": "right"})
		idFrame.pack()

		createFrame = Frame(bigFrame)
		# Create
		self.SUBMIT = Button(createFrame, text="Create", command=self.make_table, width="10")
		self.SUBMIT.pack()
		self.lblResult = Label(createFrame)
		self.lblResult.pack()
		createFrame.pack(pady=20)

		bigFrame.pack(fill=X, padx=5, pady=5)

		creditsFrame = Frame(root)
		self.btnCredits = Button(creditsFrame, text="Credits", command=self.show_credits)
		self.btnCredits.pack()
		creditsFrame.pack(side=LEFT)
		
	def getInFile(self):
		self.infilename = askopenfilename(filetypes=[("CSV files","*.csv")], title="Choose a souce...")
		self.infilename = os.path.normpath(self.infilename)
		self.lblInFilePicked["text"] = "Source: " + self.infilename

	def getOutFile(self):
		self.outfilename = asksaveasfilename(filetypes=[("HTML files","*.html *.htm")], title="Choose a destination...")
		self.outfilename = os.path.normpath(self.outfilename)
		self.lblOutFilePicked["text"] = "Destination: " + self.outfilename

	def show_credits(self):
		box.showinfo("Information", "Table Writer 0.4\n" + chr(169) + " 2012 Frederick County, VA.\nBuilt by Jeremy Coulson.\nhttps://github.com/mrcoulson/CSV-to-HTML-Table.")

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	
root = Tk()
root.minsize(width=350, height=295)
root.geometry("350x295")
root.title("CSV -> HTML Table Writer")
app = Application(master=root)
app.mainloop()