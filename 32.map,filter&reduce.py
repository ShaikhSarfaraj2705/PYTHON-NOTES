#MAP:the map function applies a function to each element in a sequence and return a new 
#sequence containing the transformed elements
def cube(x):
    return x*x*x
l=[5,3,8,1,0,7,9,4]
new=list(map(cube,l))
print(new)

#FILTER:the filter function filters a sequence of element based on a predicate(a function
#that returns a boolean value) and returns a new sequence containing only the elements
#that meet the predicate
def filter_function(a):
    return a>5
new=list(filter(filter_function,l))
print(new)

#REDUCE:the reduce function is higher-order function that applies a function to a sequence 
#and returns a single value.it is a part of the functools module in python
from functools import reduce
def sum(x,y):
    return x+y
new=reduce(sum,l)
print(new)