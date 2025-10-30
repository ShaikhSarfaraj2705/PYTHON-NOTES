#FUNCTION CACHING:function caching is a technique for improving the performance of a 
#program by storing the results of a function call so that you can reuse the results 
#instead recomputing them for every time the function is called.this can be particularly 
#useful when afunction is computationally expencive,or when the inputs to the function are 
#unlikely to change frequently.

#in python function caching can be achieved using the functools.lru_cache decorator.the 
#functools.lru_cache is used to cache the results of the function so that you can reuse 
#the results instead of recomputing them every time the function is called.

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
            
print(fx(20))
print("done for 20")
print(fx(10))
print("done for 10")
print(fx(99))
print("done for 99")


print(fx(20))
print("done for 20")
print(fx(10))
print("done for 10")
print(fx(99))
print("done for 99")
print(fx(4))
print("done for 4")