import os

from operator import itemgetter, attrgetter 

def month_to_second(month_str):
	if (month_str == "January"):
		return 1
	if (month_str == "February"):
		return 2
	if (month_str == 'March'):
		return 3
	if (month_str == 'April'):
		return 4
	if (month_str == 'May'):
		return 5
	if (month_str == 'June'):
		return 6
	if (month_str == 'July'):
		return 7
	if (month_str == 'August'):
		return 8
	if (month_str == 'September'):
		return 9
	if (month_str == 'October'):
		return 10
	if (month_str == 'November'):
		return 11
	if (month_str == 'December'):
		return 12

class Date():
        def __init__(self,year,month,day,hour,minute,filenum):
                self.year = year
                self.month = month  
                self.day = day
                self.hour = hour
                self.minute = minute
                self.filenum = filenum
        def __repr__(self):  
                return repr(( self.year, self.month, self.day, self.hour, self.minute, self.filenum))  
date_list = []
date_file = []



day = 0
year = 0
hour = 0
minute = 0
month = 0

for path,folders,files in os.walk("C:\Users\sandaon\Desktop\Python\hw_5\Test_data") :
	for f in files :
		filenum = f
		a = open (os.path.join(path, f))
		for line in open (os.path.join(path, f),"r"):
			line = a.readline()
			if (line.find("Date")) == 0 :
				
				splited = line.split()

				day = splited[1]	
				month_str = splited[2]
				#Function
				month = month_to_second(month_str)		
				year = splited[3]	
				hour = (splited[5])[0:2]
				minute = (splited[5])[3:]
				date = Date(year, month, day, hour, minute, filenum)
				date_list.append(date)

a = sorted(date_list, key=attrgetter('year','month','day','hour','minute'))

for i in a:
	date_file.append(i.filenum)

open ("date.txt","w").write('%s' % "\n".join(date_file))
