a=(1,2,3,4,5,6,7,8,9,10)
b=list(a)
c=[]
for i in b:
	if i%2==0:
		c.append(i)
d=tuple(c)
print (d)