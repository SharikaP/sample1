a=input("input an array of numbers: ")
for i in a[:-1]:
	if (i+1) not in a:
		print (i+1)