a= input("Input a dog's age in human years: ")
b=0
for i in range(1, a+1):
	if (i==1 or i==2):
		b+=10.5
	else:
		b+=4
print("The dog's age in dog's years is %d" %b)		