a=["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
b=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday","","","","",""]
k=1
while (k==1):
	e=raw_input("Please enter a month or day: ")
	for i in range(0,12):
		if e==a[i]:
			print (i+1)
		elif e==b[i]:
			print (i+1)
		
	k=input("if you want to check once more, type 1, else type 0 ")