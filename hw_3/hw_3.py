money = 0
i = 0
f = open("test.txt","r")
array = []

for line in open("test.txt","r") :
	
	line = f.readline()	
	array.append(line)
	

for i in range ( 4 , len(array	) , +1 ) :

	if (array[i])[0:8] == (array[3])[0:8]:
		money += 2000000
	elif (array[i])[0:8] == (array[0])[0:8]:
		money += 200000
	elif (array[i])[0:8] == (array[1])[0:8]:
		money += 200000
	elif (array[i])[0:8] == (array[2])[0:8]:
		money += 200000
	elif (array[i])[1:8] == (array[0])[1:8]:
		money += 40000
	elif (array[i])[1:8] == (array[1])[1:8]:
		money += 40000
	elif (array[i])[1:8] == (array[2])[1:8]:
		money += 40000
	elif (array[i])[2:8] == (array[0])[2:8]:
		money += 10000
	elif (array[i])[2:8] == (array[1])[2:8]:
		money += 10000
	elif (array[i])[2:8] == (array[2])[2:8]:
		money += 10000
	elif (array[i])[3:8] == (array[0])[3:8]:
		money += 4000
	elif (array[i])[3:8] == (array[1])[3:8]:
		money += 4000
	elif (array[i])[3:8] == (array[2])[3:8]:
		money += 4000
	elif (array[i])[4:8] == (array[0])[4:8]:
		money += 1000
	elif (array[i])[4:8] == (array[1])[4:8]:
		money += 1000
	elif (array[i])[4:8] == (array[2])[4:8]:
		money += 1000
	elif (array[i])[5:8] == (array[0])[5:8]:
		money += 200
	elif (array[i])[5:8] == (array[1])[5:8]:
		money += 200
	elif (array[i])[5:8] == (array[2])[5:8]:
		money += 200

print money

