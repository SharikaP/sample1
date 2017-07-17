n=input("Input a number: ")
print (str(n)+","),
while n!=1:
	if n%2==0:
		n=n/2
		print (str(n)+","),
	elif n%2!=0:
		n=3*n+1
		print (str(n)+","),

