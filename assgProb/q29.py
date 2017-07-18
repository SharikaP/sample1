a=1
out=0
while a==1:
	trans=raw_input("Input a deposit or a withdrawal: ")
	t1=trans.split(" ")
	if t1[0]=="D" :
		out+=int(t1[1])
	elif t1[0]=="W":
		out-=int(t1[1])
	a=input("press 1 to continue or 0 to exit")
print (out) 