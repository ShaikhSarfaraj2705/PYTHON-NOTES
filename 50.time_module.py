#TIME MODULE:in python provides a set of functions to work with the time-related operations,
#such as timekeeping, formatting and time conversions.this module is the part of the python 
#standard library.

#time.time()-the time.time() functions returns the current time as a floating point number 
#representing the number of seconds since the epoch.
import time
print(time.time())
print("_________________________________________________________________________________")

#time.sleep()-the time.sleep() function suspends the execution of the current thread for a
#specified number of seconds.this function can be used to pause the program for a certain 
#period of time,allowing other parts of program to run or synchronize the execution of 
#multiple thread. 
time.sleep(5)
print("this is printed after 5 seconds.")
print("_________________________________________________________________________________")

#time.strftime()-the time.strtime() function formats a time value as a string,based on 
#specified formats.this function is particularly useful for formatting dates and times in
#a human readable format,such as for display in a GUI,a log file,or a report.
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d\n%H-%M-%S",t)
print(formatted_time)