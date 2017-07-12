x=[["" for i in range(5)] for j in range(7)]
for i in range(1,8):
	for j in range(1,6):
		if(j==1):
			x[i-1][j-1]="* "
		elif((i==7) and (j!=1)):
			x[i-1][j-1]="* "
		else:
			x[i-1][j-1]="  "
		

for i in range(1,8):
	for j in range(1,6):
		print x[i-1][j-1]+
	print ('\n')		