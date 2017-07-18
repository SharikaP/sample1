a=raw_input("Input an email address: ")
b=list(a)
def search(list,char):
	for i in range(len(list)):
		if list[i]==char:
			return i
c=search(b,'@')
d=search(b,'.')
e=[]
for i in range(c+1,d):
	e.append(b[i])
f=''.join(e)
print (f)