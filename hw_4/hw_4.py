array_x = []
array_y = []
import os

for path,folders,files in os.walk("C:\Users\sandaon\Desktop\Python\hw_4\Test_data") :

	for f in files :
		filenum = int(f[4:])
		filenum -= 1
		a = open (os.path.join(path, f))
		# print (os.path.join(path, f))
		for line in open (os.path.join(path, f),"r"):
			line = a.readline()	
			fromlist = line.find("From: ")
			tolist = line.find("To: ")

			if fromlist == 0 : 
				x = line.replace("From: ","",1)
				array_x.insert(filenum,x)

			elif tolist == 0 : 
				y = line.replace("To: ","",1)
				array_y.insert(filenum,y)	
			
		a.close

open ("Fromname.txt","w").write('%s' % "".join(array_x))
open ("Toname.txt","w").write('%s' % "".join(array_y))
