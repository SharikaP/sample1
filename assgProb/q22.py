list=[12,24,35,70,88,120,155]
list1=[]
for i in range(len(list)):
	if i%2!=0:
		list1.append(list[i])
print (list1)