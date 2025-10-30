#READLINES METHOD:the readline() method reads single line from the file.if we want to 
#read multiple lines we can use a loop
f=open('29.file_io.txt', 'r')
# contents=f.readline()
# print(contents) 
while True:
    line=f.readline()
    if not line:    
        break
    print(line)
print("_________________________________________________________________________________")

#WRITELINES METHOD:the writelines() method in python writes a sequence of strings to a 
#file. the sequence can be iterate object, such as list or tuple
f=open('29.file_io.txt', 'w')
lines=["line 1\n","line 2\n","line 3\n","line 4\n","line 5"]
f.writelines(lines)
f.close()
print("_________________________________________________________________________________")

#SEEK:the seek() function allows you to move to current position within a file to a 
#specific point.the position is specified in bytes and you can move either forward or 
#backword from the current position

#TELL:the tell() function returns the current position within the file, in bytes.this 
#can be useful for keepingtrack of your location within the file or for seeking to a 
#specific position relative to the current position
with open('29.file_io.txt', 'r') as f:
    f.seek(10)      #move to the 10th byte in the file
    current_position=f.tell()   #shows current position
    data=f.read(5)  #read the next 5 bytes
    print(data)
    print(current_position)
print("_________________________________________________________________________________")

#TRUNCATE:when you open a file in python using the open function, you can specify the mode 
#in which you want to open the file.if you specify mode as 'w' or 'a', the file is opened 
#in write mode and you can write to the file.however, if you want to truncate the file to
#a specific size, you can use the truncate function
with open('29.file_io.txt', 'w') as f:
    f.write("adding extra")
    f.truncate(6)
with open('29.file_io.txt', 'r') as f:
    print(f.read())
