#LAMBDA FUNCTION:in python,a lambda function is small anonymous function without a name.it
#is defined using lambda keyword and has the following syntax:lambda arguments:expression
cube=lambda x:x*x*x
print(cube(3))

#lambda functions are often used in situations where a small function is required for a 
#short period of time. they are commanly used as arguments to higher-order functions, such 
#as map, filter and reduce
#lambda function can have multiple arguments,just like regular functions
multiply=lambda x,y,z:x*y*z
print(multiply(13,7,2))