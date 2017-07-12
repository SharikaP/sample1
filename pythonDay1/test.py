import sys
a=sys.argv[1]
b=reversed(a)
if list(a)==list(b):
	print ("it is a palindrome")
else:
	print("it is not a palindrome")
