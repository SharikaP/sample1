def last(a):
	return a[-1]
a=input("Enter a list of tuples: ")
print sorted(a, key=last)