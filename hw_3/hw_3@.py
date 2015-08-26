f = open ("hello.txt","r")
result = list()  
for line in f:  
    line = line.readline()  
    print line  
    result.append(line)  
print result 
f.close()                  
open('result-readline.txt', 'w').write('%s' % ''.join(result))