#all permutations of [1,2,3]
a=[1,2,3]
for i in a:
	for j in a:
		for k in a:
			if (i!=j and j!=k and k!=i):
				print(str(i)+" "+str(j)+" "+str(k))