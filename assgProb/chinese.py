# a+b=35
# 2*a+4*b=94
# no.of chickens=a
# no.of rabbits=b
for i in range(36):
	for j in range(36):
		if (i+j==35 and 2*i+4*j==94):
			print ("no. of chickens are %d" %i)
			print ("no. of rabbits are %d" %j)