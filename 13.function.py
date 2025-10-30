#FUNCTION
#a function is a block of code that performs specific task whenever it is called
#there is two types of function:[a]built-in function [b]user-defined function
def average(a,b,c):
    avg=(a+b+c)/3
    print("average is:",avg)
average(42,53,11)
#built-in function:these function are defined and pre-coded in python. ex,min(),max(),type(),len(),range(),print()
#user-defined function:we can create function to perform specific task as perour needs.
print("_________________________________________________________________________________")

#FUNCTION ARGUMENTS:

#four types of  arguments that we can provide a function:<1>default argument <2>keyword argument <3>veriable length argument <4>required argument

#default arguments-we can provide default value while creating a function.
def average(x=10,y=20):
    print("average is: ",(x+y)/2)
average()   #no parameter is passed then default value is used
average(5)  #only single parameter is passed then it choose default value of second parameter
average(y=30)#when choosing second value from parameter we need to declare argumnet variable name and it choose default value from first parameter
print("_________________________________________________________________________________")

#keyword arguments-we can provide argument with key=value, hence the order in which the argumentare passed does not matter
average(y=45,x=90)
print("_________________________________________________________________________________")

#required arguments-in case if we don't pass the arguments with a key=value syntax, then it neccessory to pass the argument in correct positional order
def avg(x,y,z=34):
    print("average is: ",(x+y+z)/3)
avg(65,55)  #two value is required pass in the calling function
print("_________________________________________________________________________________")

#variable-length argument-sometimes we may need to pass more arguments than those defined in the actual function.this can be done using variable-length argument.
def _average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is: ",sum/len(numbers))
_average(53,44)
print("_________________________________________________________________________________")

#REURN STATEMENT
#the return statement is used to return the value of the expression back to the calling function
def avg(x,y,z):
    return (x+y+z)/3
print("average is: ",avg(65,55,39))    #or
c=avg(78,72,23)
print("average is: ",c)