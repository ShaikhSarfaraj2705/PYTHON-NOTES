#FILE IO-
#OPENING A FILE:before we can perform any operations on a file,we must first open it. 
#python provide open() function to open a file. it takes arguments: the name of the file 
#and the mode in which the file should be opened. the mode can be 'r' for reading, 'w'
#for writing or 'a' for appending
f=open('29.file_io.txt', 'r')

#MODES IN FILE:
#1>read(r):this mode open the file for reading only and gives an error if file does not 
#exits.this is default mode if no mode is passed as a parameter
#2>write(w):this mode open the file for writing only and create a file if does not exists
#3>append(a):this mode open the file for appending only and create a file if does not exists
#4>create(x):this mode creates a file and gives an error if the file already exists

#READING FROM A FILE:the read() method read the entire contents of the file and returns 
#it as a string.
reading=f.read()
print(reading)

#CLOSING A FILE:it is important to  close a file after you are done with it. to close a 
#file you can use the close() method
f.close()

#WRITING TO A FILE:to write a file, we first need to open it in write mode. we can then 
#use write() method to write to a file.
f=open('29.file_io.txt', 'w')
writing=f.write("this is demo.")
print(writing)
f.close()

# #APPENDING TO A FILE:
f=open('29.file_io.txt', 'a')
appending=f.write(" adding new text at the end of exiting text")
print(appending)
f.close()

# #CREATING A NEW FILE:
f=open('29.create.txt','x')
f.close()

#THE 'with' STATEMENT:alternatively, you can use the with statement to automatically 
#close the file after you are done with it.
with open('29.create.txt','r') as f:
    reading=f.read()
    print(reading)
