d=1
while (d==1):
	print("Operations which can be performed: addition, subtraction, multiplication, division")
	a=raw_input("Enter your first number: ")
	while (a.isdigit()!=True):
		a=raw_input("Please enter a number :")
	b=raw_input("Enter your second number: ")
	while (b.isdigit()!=True):
		b=raw_input("Please enter a number :")
	c=raw_input("Which operation would you like to perform? ")
	if c=="addition":
		print (float(a)+float(b))
	elif c=="subtraction":
		print (float(a)-float(b))
	elif c=="multiplication":
		print (float(a)*float(b))
	else:
		print (float(a)/float(b))
	d=input("Type 0 to exit, 1 to continue: ")