import os

sortlist = []
datelist = []
maillist = []
order = str()
error = str()


def bubbleSort(alist):  
    for passnum in range(len(alist)-1,0,-1):  
        #print alist,passnum  
        for i in range(passnum):  
            if alist[i]>alist[i+1]:  
                temp = alist[i]  
                alist[i] = alist[i+1]  
                alist[i+1] = temp  
    return alist  

def day_change(day_str):

	if (len(day_str) == 1) :
		day = "0"+ day_str
		return day
	else :
		return day_str


def month_change(month_str):
	if (month_str == "January"):
		return "01"
	if (month_str == "February"):
		return "02"
	if (month_str == 'March'):
		return "03"
	if (month_str == 'April'):
		return "04"
	if (month_str == 'May'):
		return "05"
	if (month_str == 'June'):
		return "06"
	if (month_str == 'July'):
		return "07"
	if (month_str == 'August'):
		return "08"
	if (month_str == 'September'):
		return "09"
	if (month_str == 'October'):
		return "10"
	if (month_str == 'November'):
		return "11"
	if (month_str == 'December'):
		return "12"


class Mail():
	def __init__ (self,filename,ID,fromname,toname,date):
		self.filename = filename
		self.ID = ID
		self.fromname = fromname
		self.toname = toname
		self.date = date
	def __repr__(self):
		return repr((self.filename, self.ID, self.fromname, self.toname, self.date))	



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

				elif line.find("Date") == 0 :					
					splited = line.split()
					day_str = splited[1]
					day = day_change(day_str)
					month_str = splited[2]
					#Function
					month = month_change(month_str)		
					year = splited[3]	
					hour = (splited[5])[0:2]
					minute = (splited[5])[3:]
					date = year + month + day + hour + minute

				elif line.find("Content") == 0 :
					mail = Mail(filename,ID,fromname,toname,date)
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
				break
			elif i == len(maillist)-1 and findfromname != maillist[i].fromname[:-1] :
				print "-"

	elif order[0:8] == "query -t" :
		findto = order.split('"')
		findtoname = findto[1]
		for i in range (0,len(maillist),+1) :
			if findtoname == maillist[i].toname[:-1] :
				print maillist[i].ID[:-1]
				break
			elif i == len(maillist)-1 and findtoname != maillist[i].toname[:-1] :
				print "-"

	elif order[0:8] == "query -d" :
		dateseries = order[8:].split("~")
		if len(dateseries) == 2 :

			if len(dateseries[0]) == 0 :
				for i in range (0 ,len(maillist), +1) :
					if maillist[i].date <= dateseries[1] :
						sortlist.append(maillist[i].date)
					datesorted = bubbleSort(sortlist)
				for j in range (0 , len(datesorted), +1) :
					for k in range (0 ,len(maillist), +1) :
						if datesorted[j] == maillist[k].date :
							datesorted[j] = maillist[k].ID

				for l in datesorted :
					print l,
				

			elif len(dateseries[1]) == 0 :
				for i in range (0 ,len(maillist), +1) :
					if maillist[i].date >= dateseries[0] :
						sortlist.append(maillist[i].date)
				datesorted = bubbleSort(sortlist)
				for j in range (0 , len(datesorted), +1) :
					for k in range (0 , len(maillist), +1) :
						if datesorted[j] == maillist[k].date :
							datesorted[j] = maillist[k].ID
				for l in datesorted :
					print l,

				


			elif len(dateseries[0]) and len(dateseries[1]) != 0 :
				for i in range (0 ,len(maillist),+1) :
					if maillist[i].date >= dateseries[0] and maillist[i].date <= dateseries[1] :
						sortlist.append(maillist[i].date)

				datesorted = bubbleSort(sortlist)

				for k in range (0 ,len(datesorted), +1) :
					for l in range (0 ,len(maillist), +1) :
						if datesorted[k] == maillist[l].date :
							datesorted[k] = maillist[l].ID

				for m in datesorted  :
					print m ,

			datesorted = []
			sortlist = []
		else :
				print "how can you be so pity ?"

	else :
		print "fuck"

	order = str()
	error = str()