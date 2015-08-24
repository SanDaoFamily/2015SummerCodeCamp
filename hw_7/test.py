import os

arraylist = []
maillist = []



class Mail():
	def __init__ (self,filename,ID,fromname,toname):
		self.filename = filename
		self.ID = ID
		self.fromname = fromname
		self.toname = toname
	def __repr__(self):
		return repr((self.filename, self.ID, self.toname, self.fromname))	

order = str()
error = str()

while order == str() :
	order = str(raw_input())
	if order == "exit" :
		break
	if order[0:4] == "add " :
		for i in range (0, len(maillist), +1) :
			if order[4:] == maillist[i].filename :
				error = "error"
				print "You silly ,fuck you !"
				break
			
		print order[8:]

		filename = order[4:]
		
		for path,folders,files in os.walk("C:\Users\sandaon\Desktop\Python\hw_7\Test_data2") :
			
			if error == "error" :
				break
			a = open (os.path.join(path, filename),'r')

			for line in open (os.path.join(path, filename),'r') :

				line = a.readline()

				if 	line.find("Message-ID") == 0 :
					ID = line.replace("Message-ID: ","",1)

				elif line.find("From: ") == 0 :
					fromname = line.replace("From: ","",1)

				elif line.find("To: ") == 0 :
					toname = line.replace("To: ","",1)

					mail = Mail(filename,ID,fromname,toname)
					maillist.append(mail)



	elif order[0:7] == "remove " :
		removeID = order[7:]


		for i in range (0, len(maillist),+1) :	

			if removeID == maillist[i].ID[:-1] :
				del maillist[i]
				print removeID
				break
			elif i == len(maillist)-1 and removeID != maillist[i].ID[:-1] :
				print "-"


	elif order[0:8] == "query -f" :
		findfrom = order.split('"')
		findfromname = findfrom[1]
		for i in range (0,len(maillist),+1) :

			if  maillist[i].fromname[:-1] == findfromname:
				print maillist[i].ID[:-1]
			elif i == len(maillist)-1 and findfromname != maillist[i].fromname[:-1] :
				print "-"

	elif order[0:8] == "query -t" :
		findto = order.split('"')
		findtoname = findto[1]
		for i in range (0,len(maillist),+1) :
			if findtoname == maillist[i].toname[:-1] :
				print maillist[i].ID[:-1]
			elif i == len(maillist)-1 and findtoname != maillist[i].toname[:-1] :
				print "-"


	else :
		print "fuck"
	order = str()
	error = str()


print maillist