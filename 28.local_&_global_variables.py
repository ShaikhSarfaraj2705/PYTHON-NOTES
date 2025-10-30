#LOCAL VARIABLE:is a variable that is defined within the function and is only accessible 
#within that function. it is created when function is called and is destroyed when the 
#functions returns

#GLOBAL VARIABLE:is a variable that is defined outside of the function and is accessible 
#from within any function in your code

#GLOBAL KEYWORD:is used to declare that a variable is a global variable and should be 
#accessed from the global scope

a=24    #global variable
print("a:",a)
def var():
    global a
    a=82
    b=78    #local variable
    print("a:",a)
    print("b:",b)
var()
print("a:",a)
#print("b:",b)  #this will cause error because b is a local variable and is not 
                #accessible outside of a function
