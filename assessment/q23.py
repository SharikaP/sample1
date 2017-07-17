filename=raw_input("Enter file name to be opened: ") #inputting the file name
fopen=open(fileName, "a") #opening the file to be changed
a=raw_input("Enter the string to be appended: ") #inputting the string to be appended
fopen.write(a) #appending that string to the file
fopen.close() #closing the file
