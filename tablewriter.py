from tkinter import *
import csv

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
			except:
				# Show type error.
				self.lblResult["text"] = "Error. Make sure your columns value is either blank or an integer."
				self.lblResult["fg"] = "#ef102a"
				# Do this better.
		
		infilename = self.txtInfile.get()
		outfilename = self.txtOutfile.get()

		try:
			with open(infilename, "r") as infile:
				with open(outfilename, "w") as outfile:
		
					# Write some HTML.
					outfile.write("<!-- START COPYING HTML HERE. -->\n")
					outfile.write("<table>\n")

					# Loop for table.
					rownum = 0
					for row in csv.reader(infile):
						if rownum == 0: # Write th row.
							outfile.write("\t<tr>\n")
							colnum = 0
							for column in row:
								colnum += 1
								if includeColumns > 0:
									if colnum < includeColumns:
										outfile.write("\t\t<th>" + column + "</th>\n")
								else:
									outfile.write("\t\t<th>" + column + "</th>\n")
							outfile.write("\t</tr>\n")
							rownum += 1
						else: # Write other rows.
							outfile.write("\t<tr>\n")
							colnum = 0
							for column in row:
								colnum += 1
								if includeColumns > 0:
									if colnum < includeColumns:
										outfile.write("\t\t<td>" + column + "</td>\n")
								else:
									outfile.write("\t\t<td>" + column + "</td>\n")
							outfile.write("\t</tr>\n")
							rownum += 1

					# Finish table.
					outfile.write("</table>\n")
					outfile.write("<!-- STOP COPYING HTML HERE. -->")

					# Show records written.
					self.lblResult["text"] = "Finsihed. " + str(rownum) + " records written."
					self.lblResult["fg"] = "#007f3f"
		except:
			# Show type error.
			self.lblResult["text"] = "Error. Make sure the source file path is correct."
			self.lblResult["fg"] = "#ef102a"
			# Do this better.

	def createWidgets(self):

		self.lblInfile = Label(self, text="Source file:")
		self.lblInfile.pack()

		self.txtInfile = Entry(self, width="50", text="newaddressing.csv")
		self.txtInfile.pack()

		self.lblOutfile = Label(self, text="Destination file:")
		self.lblOutfile.pack()

		self.txtOutfile = Entry(self, width="50")
		self.txtOutfile.pack()

		self.lblColumns = Label(self, text="Columns to include (leave blank to include all):")
		self.lblColumns.pack()

		self.txtColumns = Entry(self, width="50")
		self.txtColumns.pack()

		self.SUBMIT = Button(self, text="Create", command=self.make_table)
		self.SUBMIT.pack()

		self.lblResult = Label(self)
		self.lblResult.pack()

	def onError(self):
		box.showerror("Error", "Bummer.")

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	
root = Tk()
root.minsize(width=350, height=175)
root.geometry("350x175")
app = Application(master=root)
app.mainloop()