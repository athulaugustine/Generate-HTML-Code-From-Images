class Builder():
	def __init__(self):
		self.file=open("html/index.html","w")
		self.file2=open("html/main.css","w")
		self.file.write("<html>")
		self.file.write("\n")
		self.file.write("<head>")
		self.file.write("\n")
		self.file.write("<link rel="+'''"'''+"stylesheet"+'''"'''+" type="+'''"'''+"text/css"+'''"'''+" href="+'''"'''+"main.css"+'''"'''+">")
		self.file.write("\n")
		self.file.write("</head>")
		self.file.write("<body>")
		self.file.write("\n")
		self.index=0
	def button(self,y,x,width,height,string):
		print "INVOKED"+str(x)+" "+str(y)
		self.idvariable="id"+str(self.index)
		self.index=self.index+1
		self.file.write("<button id="+'''"'''+self.idvariable+'''"'''+" type="+"button"+">"+string+"</button>")
		self.file.write("\n")
		string="#"+self.idvariable+"{"
		self.file2.write("\n")
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("position: absolute;")
		self.file2.write("\n")
		string="top:"+str(x)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		string="left:"+str(y)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("}")

	def close(self):
		self.file.write("</body>")
		self.file.write("\n")
		self.file.write("</html>")
		self.file.write("\n")
	def table(self,row,column,y,x):
		self.idvariable="id"+str(self.index)
		self.index=self.index+1
		self.file.write("<table border="+'''"'''+str(1)+'''"'''+"id="+'''"'''+self.idvariable+'''"'''+">")
		self.file.write("\n")
		for i in range(row-1):
			self.file.write("\n")
			self.file.write("<tr>")
			self.file.write("\n")
			for j in range(column-1):
				self.file.write("<td>test</td>")
				self.file.write("\n")
			self.file.write("</tr>")
			self.file.write("\n")
		self.file.write("\n")
		self.file.write("</table>")
		#Now CSS File
		self.file2.write("\n")
		string="#"+self.idvariable+"{"
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("position: absolute;")
		self.file2.write("\n")
		string="top:"+str(x)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		string="left:"+str(y)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("}")
	def textbox(self,y,x,string):
		self.idvariable="id"+str(self.index)
		self.index=self.index+1
		if string.lower()=="EMAIL".lower():
			self.file.write("<input "+"id="+'''"'''+self.idvariable+'''" '''+"type="+'''"'''+"email"+'''" '''+"value="+'''"'''+"Enter your Email"+'''"'''+">")
		if string.lower()=="PASSWORD".lower():
			self.file.write("<input "+"id="+'''"'''+self.idvariable+'''" '''+"type="+'''"'''+"password"+'''" '''+">")
		self.file.write("\n")
		string="#"+self.idvariable+"{"
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("position: absolute;")
		self.file2.write("\n")
		string="top:"+str(x)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		string="left:"+str(y)+"px;"
		self.file2.write(string)
		self.file2.write("\n")
		self.file2.write("}")


