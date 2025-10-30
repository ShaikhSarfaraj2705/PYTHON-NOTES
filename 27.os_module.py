#OS MODULE:the os module in python is a built-in library that provide functions for 
#interacting with the operating system.it allows you to perform wide variety of tasks,
#such as a reading writing files, int eracting with the file system and running the system commands
import os

if(not os.path.exists("100 days")): #to create a file in specific location
    os.mkdir("26.os_module")

for i in range(0,50):               #to create multiple files
    # os.mkdir(f"26.os_module/example {i+1}")
    # os.rename(f"26.os_module/example {i+1}", f"26.os_module/demo {i+1}")    #to change file name

 folders=os.listdir("26.os_module") #to show lists of files
for file in folders:
    print(file)

for file in folders:                #showing contents in file
   print(file)
   print(os.listdir(f"26.os_module/{file}"))

print(os.getcwd())                  #to get the diectory path
os.chdir("26.os_module")            #to change the directory path
print(os.getcwd())