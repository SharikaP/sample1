list=[12,24,35,24,88,120,155,88,120,155]
list1=[]
a=set()
for i in list:
	if i not in a:
		a.add(i)
		list1.append(i)
print(list1[::-1])

