a=["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
b=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
c=[1,2,3,4,5,6,7,8,9,10,11,12]
d=[1,2,3,4,5,6,7]
e=raw_input("Please enter a month or day: ")
for i in range(0,12):
	if e==a[i]:
		print c[i]
	elif e==b[i]:
		print d[i]