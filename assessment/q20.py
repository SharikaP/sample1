a=raw_input("Input a string: ")
list=a.split(" ") #string to list-separated by space
set=set(list) #list to set to get the distinct elements
for i in set:
	print(str(i)+":"+str(list.count(i)))

