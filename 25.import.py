#IMPORT:importing in python is the process of loading code from a python module into the 
#current script.this allows you to use the functions and variables defined in the module in 
#your current script, as well as any additional modules that the imported module may depend on.
#To import a module in python, you use import statement followed by the name of the module.
import math 
print(math.sqrt(75))

#FROM KEYWORD:you can also import a specific functions or variables from a module using the from keyword
from math import factorial,pi
result= factorial(5)+pi
print(result)

#IMPORTING EVERYTHING:it's also possible to import all functions and variables from a module using the *wildcard
from math import *
result=floor(4.5673)+pi+sqrt(74)
print(result)

#THE 'as' KEYWORD
import math as m
print(m.factorial(65))
from math import sqrt as s
print(s(89))

#THE dir FUNCTION:python has built-in function called dir that you can use to view the
#names of all functions and variables  defined in a module
import math 
print(dir(math))