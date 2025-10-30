#GENERATORS:generators in python are special type of functions that allows you to create 
#an iterable sequence of values.a generator function that return a generator object,which 
#can be used to generate the values one-by-one as you iterate over it.generator are 
#powerful tool for working with large of complex data set ,as they allow you to generate
#the values on-the-fly,rather than having to create and store the entire sequence in a memory.

#you can create a generator  by using the yield statement in the function.the yield statements
#returns a value from the generator and suspends the execution of the function until the 
#next value is requested.
 
def my_generators():
    for i in range(500):
        yield i
gen=my_generators()
print(next(gen))
print(next(gen))
print(next(gen))
#we can also print using for loop
# for j in gen:
#     print(j)