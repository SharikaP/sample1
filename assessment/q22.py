a=raw_input("input a sentence: ")
l=0
d=0
for i in a:
	if i.isdigit()==True:
		d+=1
	elif i.isalpha()==True:
		l+=1
print ("LETTERS %d" %l)
print ("DIGITS %d" %d)