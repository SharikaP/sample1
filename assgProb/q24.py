a=raw_input("Input a string comprising of numbers and words: ")
b=a.split(" ")
c=[]
for i in b:
	if i.isdigit()==True:
		c.append(i)
print c
	