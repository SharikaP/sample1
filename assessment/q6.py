a=raw_input("Enter an email address: ")
l=list(a)
l1=[]
for i in a:
	if i!='@':
		l1.append(i)
	else:
		break
uName=''.join(l1)
print (uName)
		