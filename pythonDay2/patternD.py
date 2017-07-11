x=[["" for i in range(5)] for j in range(7)]
for i in range(1,8):
	for j in range(1,6):
		if((i==1 or i==7) and(j==2 or j==3 or j==4)):
			x[i-1][j-1]="* "
		elif(j==1):
			x[i-1][j-1]="* "
		elif((i!=1 and i!=7)and(j==5)):
			x[i-1][j-1]="* "
		else:
			x[i-1][j-1]="  "
		

for i in range(1,8):
	for j in range(1,6):
		print x[i-1][j-1],
	print ('\n')		