
lis=raw_input("enter a list of passwords: ")
li=lis.split(',')
l1=[]
for password in li:
		a=any(x.isdigit() for x in password) #checking for the presence of atleast 1 digit
		b=any(x.isupper() for x in password) #checking for the presence of atleast 1 uppercase letter
		c=any(x.islower() for x in password) #checking for the presence of atleast 1 lowercase letter
		d=all([len(password)>=6,len(password)<=16]) #criteria for length of a password
		e=any(x in "[$#@]" for x in password) #checking for the presence of a special character
		if all([a,b,c,d,e])==True:
			l1.append(password)
print (l1)
