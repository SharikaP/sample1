password=raw_input("enter your password ")
a=any(x.isdigit() for x in password)
b=any(x.isupper() for x in password)
c=any(x.islower() for x in password)
d=all([len(password)>=6,len(password)<=16])
e=any([password.find('$'), password.find('#'), password.find('@')])
if all([a,b,c,d,e])==True:
	print("Your password is valid")
else:
	print("invalid. please change it")