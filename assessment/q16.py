fname=raw_input("input the file name: ")
nlines=0
with open(fname, 'r') as fo:
	for linr in fo:
		nlines+=1
print ("no.of lines: "+str(nlines))