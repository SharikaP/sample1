a=raw_input("Enter a string: ")
b=list(set(a))
for i in b:
	print (i+","+str(a.count(i)))
